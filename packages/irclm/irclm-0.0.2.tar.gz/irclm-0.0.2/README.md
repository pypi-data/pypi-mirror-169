IRC Log Manager
===============

Manage a local cache of irc logs.

Capabilities:
=============

- incremental cache update by default
- convenience wrapper for grep
- log cache optionally managed by git
- session reuse

Incremental Update
------------------

```bash
irclm
```

Conveniently Grep Log Cache
---------------------------

run command from log cache directory

```bash
irclm - grep <key>
irclm - rg <key>
irclm - git grep <key>
```

Development:
============

```bash
git clone git@github.com:holmanb/irclm.git
cd irclm
poetry install
<edit>

# run tests
poetry run all
<submit pr>
```

Goals:
======
- be simple, reliable, slim
- good netizinship - defaults to keep the servers happy

Server Support:
===============
- irclogs.ubuntu.com
- Open a PR (or a bug with details) for support!

Future Work:
============
- manifest should store per-channel updated dates
- tests, tests, tests
- verify timer install and document
