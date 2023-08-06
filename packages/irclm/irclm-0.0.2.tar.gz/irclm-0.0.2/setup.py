# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['irclm']

package_data = \
{'': ['*']}

install_requires = \
['aiohttp>=3.8.3,<4.0.0',
 'black>=22.8.0,<23.0.0',
 'flake8>=5.0.4,<6.0.0',
 'isort>=5.10.1,<6.0.0',
 'pylint>=2.15.3,<3.0.0',
 'toml>=0.10.2,<0.11.0']

entry_points = \
{'console_scripts': ['irclm = irclm.irclm:main']}

setup_kwargs = {
    'name': 'irclm',
    'version': '0.0.2',
    'description': '',
    'long_description': 'IRC Log Manager\n===============\n\nManage a local cache of irc logs.\n\nCapabilities:\n=============\n\n- incremental cache update by default\n- convenience wrapper for grep\n- log cache optionally managed by git\n- session reuse\n\nIncremental Update\n------------------\n\n```bash\nirclm\n```\n\nConveniently Grep Log Cache\n---------------------------\n\nrun command from log cache directory\n\n```bash\nirclm - grep <key>\nirclm - rg <key>\nirclm - git grep <key>\n```\n\nDevelopment:\n============\n\n```bash\ngit clone git@github.com:holmanb/irclm.git\ncd irclm\npoetry install\n<edit>\n\n# run tests\npoetry run all\n<submit pr>\n```\n\nGoals:\n======\n- be simple, reliable, slim\n- good netizinship - defaults to keep the servers happy\n\nServer Support:\n===============\n- irclogs.ubuntu.com\n- Open a PR (or a bug with details) for support!\n\nFuture Work:\n============\n- manifest should store per-channel updated dates\n- tests, tests, tests\n- verify timer install and document\n',
    'author': 'Brett Holman',
    'author_email': 'bholman.devel@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7.2,<4.0.0',
}


setup(**setup_kwargs)
