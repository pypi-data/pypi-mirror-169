#!/usr/bin/env python3
import asyncio
import json
import os
import shutil
import sys
import time
from abc import abstractmethod
from argparse import ArgumentError, ArgumentParser, Namespace
from contextlib import suppress
from datetime import date, datetime, timedelta
from functools import partial
from getpass import getuser
from grp import getgrgid
from logging import (WARNING, Formatter, Logger, StreamHandler, getLogger,
                     handlers)
from os import getgid
from pathlib import Path
from subprocess import DEVNULL, run
from textwrap import dedent
from typing import Callable, Generator, Optional
from urllib.parse import quote

import aiohttp
import toml

JSON_VERSION = 1
VERSION = "0.0.2"
PROGRAM_NAME = "irclm"
THREADS = 6
TODAY = date.today()
USER = getuser()
GROUP = getgrgid(getgid()).gr_name
REPO = "https://github.com/holmanb/irclm"

CACHE_PATH = Path.home() / ".cache" / PROGRAM_NAME
CONFIG_PATH = Path.home() / ".config" / PROGRAM_NAME
CONFIG_FILE = f"{PROGRAM_NAME}.toml"
LOG_FILE = f"{PROGRAM_NAME}.log"
MANIFEST_FILE = "Manifest.json"
LOG_NAME = f"{PROGRAM_NAME}.log"
LOG_SIZE = 1 << 23  # 8 MiB
SYSTEMD_PATH = Path.home() / ".config/systemd/user/"
SYSTEMD_SERVICE_FILE = f"{SYSTEMD_PATH}/{PROGRAM_NAME}.service"
SYSTEMD_TIMER_FILE = f"{SYSTEMD_PATH}/{PROGRAM_NAME}.timer"

SYSTEMD_SERVICE_FILE_CONTENT = dedent(
    f"""\
    [Unit]
    Description=Update log cache daily using {PROGRAM_NAME}
    Wants={PROGRAM_NAME}.timer

    [Service]
    Type=oneshot
    ExecStart={PROGRAM_NAME}
    User={USER}
    Group={GROUP}
"""
)

SYSTEMD_TIMER_FILE_CONTENT = dedent(
    f"""\
    [Unit]
    Description=Triggers irc log update
    Requires={PROGRAM_NAME}.service

    [Timer]
    Unit={PROGRAM_NAME}.service
    OnCalendar=*-*-* *:59:00
    RandomizedDelaySec=3600

    [Install]
    WantedBy=timers.target
"""
)

DEFAULT_CONFIG = dedent(
    f"""\
    [{PROGRAM_NAME}]
    cache_dir = "{CACHE_PATH}"

    [{PROGRAM_NAME}.servers]
    [{PROGRAM_NAME}.servers.ubuntu]
    name = "ubuntu"
    channels = []

    # yyyy-mm-dd
    start_date = "2004-07-05"
"""
)

SourceGenerator = Generator[str, str, str]
getLogger("urllib3").setLevel(WARNING)


def init_dirs(config):
    with suppress(FileExistsError):
        os.makedirs(config.cache)
    with suppress(FileExistsError):
        os.makedirs(Path(config.config).parent)
    with suppress(FileExistsError):
        os.makedirs(SYSTEMD_PATH)
    with suppress(FileExistsError):
        open(
            (Path(config.cache) / PROGRAM_NAME).with_suffix(".log"),
            "xt",
            encoding="utf-8",
        ).close()


class ColorizedFormatter(Formatter):
    """
    based on:
    stackoverflow.com/questions/384076/how-can-i-color-python-logging-output
    """

    BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE = range(8)
    COLORS = {
        "WARNING": YELLOW,
        "INFO": WHITE,
        "DEBUG": BLUE,
        "CRITICAL": YELLOW,
        "ERROR": RED,
    }
    RESET_SEQ = "\033[0m"
    COLOR_SEQ = "\033[1;%dm"
    BOLD_SEQ = "\033[1m"

    def __init__(self, fmt, use_color=True, **kwargs):
        Formatter.__init__(self, self.formatter_message(fmt), **kwargs)
        self.use_color = use_color

    def format(self, record):
        levelname = record.levelname
        if self.use_color and levelname in self.COLORS:
            record.levelname = (
                self.COLOR_SEQ % (30 + self.COLORS[levelname])
                + levelname
                + self.RESET_SEQ
            )
        return Formatter.format(self, record)

    @classmethod
    def formatter_message(cls, message, use_color=True):
        if use_color:
            message = message.replace("$RESET", cls.RESET_SEQ).replace(
                "$BOLD", cls.BOLD_SEQ
            )
        else:
            message = message.replace("$RESET", "").replace("$BOLD", "")
        return message


def get_logger(level: str, log_path: str):
    log = getLogger(PROGRAM_NAME)
    log.setLevel(10 * int(level))
    console_formatter = ColorizedFormatter(
        fmt="%(levelname)s %(funcName)s:%(lineno)d %(message)s"
    )
    console = StreamHandler()
    console.setFormatter(console_formatter)

    file_formatter = Formatter(
        fmt="%(asctime)s %(levelname)s %(funcName)s:%(lineno)d %(message)s"
    )
    file = handlers.RotatingFileHandler(log_path, maxBytes=LOG_SIZE)
    file.setFormatter(file_formatter)

    log.addHandler(console)
    log.addHandler(file)
    return log


class Stats:
    def __init__(self):
        self.counters = {}
        self.times = {}
        self.start = time.time()

    def increment(self, counter: str):
        self.counters[counter] = stats.counters.get(counter, 0) + 1

    def time(self, name: str, functor: Callable):
        """execute functor and add time to key stats"""
        current = self.times.get(name, 0)
        old = time.time()
        out = functor()
        new = time.time()
        delta = new - old
        self.times[name] = current + delta
        return out

    def __str__(self):
        t = time.time()
        total_time = t - self.start
        msg = "Time:\n"
        for name, counter_total in self.times.items():
            out = f" [{name}] took {counter_total:.1f}s "
            out += f"out of {total_time:.1f}s "
            out += f" {100 * counter_total / total_time:.0f}%\n"
            if not msg:
                msg = out
            else:
                msg += out
        msg += "\nCounters:\n"
        for name, counter_total in self.counters.items():
            msg += f" {name}: {counter_total}\n"

        return f"\n{40 * '='}\n{msg}"


stats = Stats()


class File:
    """File wrapper object for registration, and logging"""

    def __init__(self, path):
        self.name = path

    def write(self, content):
        stats.increment("file_written")
        with open(self.name, "wt", encoding="utf-8") as fh:
            fh.write(content)

    def read(self):
        stats.increment("file_read")
        with open(self.name, "rt", encoding="utf-8") as fh:
            content = fh.read()
        return content


def subp(args, log, cwd, **kwargs):
    out = run(args, cwd=cwd, **kwargs)
    if out.returncode != 0:
        if out.stdout:
            log.warning(out.stdout)
        if out.stderr:
            log.warning(out.stderr)
    return out


class Manifest(File):
    """self-managed persistent state object"""

    last_update: Optional[date] = None

    def __init__(
        self, cache_path: str, log, manifest_name=MANIFEST_FILE, log_name=LOG_FILE
    ):
        manifest_path = f"{cache_path}/{manifest_name}"
        super().__init__(manifest_path)
        log_path = f"{cache_path}/{log_name}"
        self.log = log
        self.store = [manifest_path, log_path]
        self.file = File(manifest_path)
        self.cache_path = cache_path
        self.has_git = not subp(
            ["git", "--version"], log, cache_path, stdout=DEVNULL, stderr=DEVNULL
        ).returncode
        if not self.has_git:
            log.warning("Install git for file management")
        if Path(manifest_path).is_file():
            self.load()
        if not Path(CACHE_PATH / ".git").is_dir():
            subp(["git", "init"], log, cache_path)

    def load(self):
        data = {
            "version": JSON_VERSION,
            "time": time.time(),
            "date_updated": (TODAY.year, TODAY.month, TODAY.day),
        }
        json_file = json.loads(self.file.read())
        new_version = data["version"]
        old_version = json_file["version"]
        self.last_update = date(*json_file["date_updated"])
        self.log.info(f"Last updated date: {self.last_update}")
        if old_version != new_version:
            self.log.warning(f"version changed from {old_version} to {new_version}")

    def save(self):
        if not self.last_update:
            self.log.info("Nothing to save")
            return
        data = {
            "version": JSON_VERSION,
            "time": time.time(),
            "date_updated": (
                self.last_update.year,
                self.last_update.month,
                self.last_update.day,
            ),
        }
        self.file.write(json.dumps(data, sort_keys=True))
        if self.has_git:
            for file in self.store:
                stats.increment("git_add")
                subp(["git", "add", str(file)], self.log, self.cache_path)

            stats.increment("git_commit")
            subp(["git", "commit", "-m", "auto"], self.log, self.cache_path)
        self.log.info(f"Saving manifest {self.file.name}")

    def register_file(self, file: File):
        stats.increment("file_register")
        self.store.append(file.name)


class Channel:
    start_date: date

    def __init__(
        self,
        name: str,
        base_url: str,
        channels: list,
        manifest: Manifest,
        log: Logger,
        start_date: str = "",
    ):
        self.name = name
        self.base_url = base_url
        self.channels = channels
        self.manifest = manifest
        self.log = log
        self.session: Optional[aiohttp.ClientSession] = None
        if start_date:
            self.start_date = datetime.strptime(start_date, "%Y-%m-%d").date()

    def write_file(self, file: str, text: str):
        f = File(file)
        f.write(text)
        self.manifest.register_file(f)

    async def respond(
        self, code: int, url: str, text: str, directory: str, file_path: str
    ):
        if 200 == code:
            self.log.info(f"Get: {url}")
            with suppress(FileExistsError):
                os.makedirs(directory)
            stats.time("write", partial(self.write_file, file_path, text))
        else:
            self.log.warning(f"BAD: {url}")

    def get_all_channels(self, start_date=None):
        for channel in self.channels:
            self.get_channel(channel, start_date)

    def get_channel(self, channel, start_date=None):
        return (
            asyncio.get_event_loop_policy()
            .get_event_loop()
            .run_until_complete(self.async_get_channel(start_date, channel))
        )

    async def async_get_channel(self, start_date: Optional[date], channel: str):
        if not self.session:
            self.session = aiohttp.ClientSession()
        for url, dir_path, file in self.gen(start_date or self.start_date, channel):
            directory = f"{CACHE_PATH}/{dir_path}"
            file_path = f"{CACHE_PATH}/{dir_path}{file}"
            async with self.session.get(url) as response:
                text = await response.text()
                await self.respond(response.status, url, text, directory, file_path)

    @abstractmethod
    def gen(self, d: date, channel: str) -> SourceGenerator:
        pass


class Ubuntu(Channel):
    start_date = date(2004, 7, 5)

    def gen(self, d: date, channel: str):
        quoted = quote(channel)
        url = f"{self.base_url}/{d.year}/{d.month:02}/{d.day:02}/{quoted}.txt"
        directory = f"{self.name}/{d.year}/{d.month}/{d.day}"
        file = f"{channel}.txt"
        yield url, directory, file


# https://stackoverflow.com/questions/1060279/iterating-through-a-range-of-dates-in-python
def date_range(start_date: date, end_date: date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)


def make_server(server: dict, manifest: Manifest, log: Logger):
    name = server["name"]
    if name.lower() == "ubuntu":
        start_date = server["start_date"]
        return Ubuntu(
            "ubuntu",
            "https://irclogs.ubuntu.com/",
            server["channels"],
            manifest,
            log,
            start_date,
        )
    log.error(f"Server definition {name} not implemented, please file a bug at {REPO}")


def get_log_range(log, args, manifest: Manifest, start_date=None):
    try:
        server_list = []
        for _, server in args.servers.items():
            server_list.append(make_server(server, manifest, log))

        # if we loaded a start date from the manifest, use that it
        # otherwise use earliest
        start = start_date or min(d.start_date for d in server_list)
        for d in date_range(start, TODAY):
            for server in server_list:
                for channel in server.channels:
                    log.debug("Getting channel:")
                    log.debug(f"name: {channel}")

                    # future optimization opportunity
                    # -------------------------------
                    # rather than getting all channels for one server followed
                    # by all for the next server, perhaps interleave calls
                    # together. This would probably help anyone whose download
                    # speed exceeds server upload speed. Not worthwhile until
                    # >1 server types are supported.
                    server.get_all_channels(d)
            manifest.last_update = d
        manifest.save()
    except KeyboardInterrupt:
        manifest.save()
    if args.stats:
        print(stats)


def refresh(log: Logger, args: Namespace, manifest: Manifest):
    get_log_range(log, args, manifest)


def update(log: Logger, args: Namespace, manifest: Manifest, start_time):
    get_log_range(log, args, manifest, start_time)


def clean(log, args):
    log.info(f"Deleting cache stored at {args.cache}")
    shutil.rmtree(args.cache)


def install_updater(log, args):
    if subp(["systemctl", "--version"], log, args.cache).returncode:
        raise NotImplementedError(
            "Service not supported on this platform, please file a bug"
        )
    log.info(f"Writing to {SYSTEMD_SERVICE_FILE}")
    log.info(f"Writing to {SYSTEMD_TIMER_FILE}")
    cwd = args.cache
    with open(SYSTEMD_SERVICE_FILE, "wt", encoding="utf-8") as f:
        f.write(SYSTEMD_SERVICE_FILE_CONTENT)
    with open(SYSTEMD_TIMER_FILE, "wt", encoding="utf-8") as f:
        f.write(SYSTEMD_TIMER_FILE_CONTENT)
    subp(["systemctl", "--user", "daemon-reload"], log, cwd)
    subp(["systemctl", "--user", "--now", "enable", f"{PROGRAM_NAME}.timer"], log, cwd)


def disable_updater(log, args):
    subp(
        ["systemctl", "--user", "--now", "disable", f"{PROGRAM_NAME}.timer"],
        log,
        args.cache,
    )


def uninstall_updater(log, args):
    log.info(f"Removing {SYSTEMD_SERVICE_FILE}")
    log.info(f"Removing {SYSTEMD_TIMER_FILE}")
    clean(log, args)
    os.remove(SYSTEMD_SERVICE_FILE)
    os.remove(SYSTEMD_TIMER_FILE)


def get_config(args) -> dict:
    config_path = args.config or CONFIG_PATH
    file_path = f"{config_path}/{CONFIG_FILE}"
    if Path(file_path).exists():
        if Path(file_path).is_file():
            print(f"Loading config from {file_path}")
            with open(file_path, "rt", encoding="utf-8") as f:
                return toml.load(f)
        else:
            sys.stderr.write(
                f"{file_path} exists, but is not a file. Cannot proceed.\n"
            )
            sys.exit(1)
    else:
        response = input("No config found. Create one at " f"{file_path}? Y/n ") or "y"
        create = response[0].lower()
        if "y" == create:
            with suppress(FileExistsError):
                os.makedirs(Path(file_path).parent)
            with open(file_path, "wt", encoding="utf-8") as f:
                f.write(DEFAULT_CONFIG)
                print(f"Wrote {file_path}, {len(DEFAULT_CONFIG.encode('utf-8'))} bytes")
            print("\nConfigure channels in the config file and try again")
        else:
            print("Config required to run. Please create a config")
        sys.exit(0)


def combined_config(args, config) -> Namespace:
    if not config:
        print("No configuration found")
    base = config[PROGRAM_NAME]

    if not args.cache:
        args.cache = base["cache_dir"]
    args.servers = base["servers"]
    return args


def cli():
    parser = ArgumentParser(
        prog="{PROGRAM_NAME} - IRC Log Manager",
        description="Manages a local archive of irc logs for grepping.",
        exit_on_error=False,
        add_help=False,
    )

    service = parser.add_subparsers(title="commands", metavar="")
    parser.add_argument(
        "--debug",
        choices=("1", "2", "3", "4", "5"),
        default="2",
        help="debug level (lower is more verbose)",
    )
    parser.add_argument("--stats", action="store_true", help="verbose stats counters")
    parser.add_argument("--config", default="", help="path to file path")
    parser.add_argument("--cache", default="", help="path to store logs")

    u = parser.add_mutually_exclusive_group()
    u.add_argument(
        "--update", action="store_true", help="[default] update files since last run"
    )
    u.add_argument("--refresh", action="store_true", help="update all logs")
    u.add_argument("--clean", action="store_true", help="drop cache")
    u.add_argument("--version", "-v", action="store_true", default=False)
    u.add_argument("--help", "-h", action="store_true", help="parser")

    # demarc the end of irclm args and the beginning of the command with '-'
    #
    #   irclm - grep <keyword>
    #
    with suppress(ArgumentError):
        service.add_parser("-", help="run command following '-' from log archive dir")
        args, unknown = parser.parse_known_args()
        if unknown:
            return args, unknown, parser

    s = service.add_parser(
        "service", help="[experimental] install/disable/uninstall a daily update timer"
    )
    g = s.add_mutually_exclusive_group()
    g.add_argument("--install", action="store_true", help="installs daemon")
    g.add_argument("--disable", action="store_true", help="disable daemon")
    g.add_argument("--uninstall", action="store_true", help="uninstalls daemon")

    # reserve the server attribute
    args = parser.parse_args(namespace=Namespace(servers=[]))

    return args, [], parser


# TODO: Clean up function signatures.
def main():
    args, unknown, parser = cli()
    if args.help:
        parser.print_help()
        print(f"\nafter editing your {CONFIG_FILE}:\n")
        print(f"  {PROGRAM_NAME}                  # download logs")
        print(f"  {PROGRAM_NAME} - grep <key>     # search logs")
    elif args.version:
        print(VERSION)
    elif unknown:
        try:
            cwd = args.cache or CACHE_PATH
            print(f"Running command [{' '.join(unknown)}] from cwd={cwd}")

            result = run(unknown, cwd=cwd)
            if result.stdout:
                print(result.stdout)
                print(f"stdout: {result.stdout}")
            if result.stderr:
                print(f"stderr: {result.stderr}")
            sys.exit(result.returncode)
        except FileNotFoundError as e:
            sys.stdout.write(f"Invalid argument: [{' '.join(unknown)}]{e}\n")
            sys.exit(1)
    else:
        args = combined_config(args, get_config(args))

        init_dirs(args)
        log = get_logger(args.debug, f"{args.cache}/{LOG_NAME}")
        manifest = Manifest(args.cache, log)

        log.debug(f"config path: {args.config}")
        log.debug(f"cache path: {args.cache}")
        if hasattr(args, "install"):
            if args.install:
                install_updater(log, args)
            elif args.disable:
                disable_updater(log, args)
            elif args.uninstall:
                uninstall_updater(log, args)
        elif args.clean:
            clean(log, args)
        elif args.refresh:
            refresh(log, args, manifest)
        elif args.update:
            update(log, args, manifest, manifest.last_update)
        else:
            update(log, args, manifest, manifest.last_update)


if __name__ == "__main__":
    main()
