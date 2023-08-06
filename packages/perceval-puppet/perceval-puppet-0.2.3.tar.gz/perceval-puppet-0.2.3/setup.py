# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['perceval', 'perceval.backends.puppet', 'tests']

package_data = \
{'': ['*'], 'tests': ['data/puppetforge/*']}

install_requires = \
['grimoirelab-toolkit>=0.3', 'perceval>=0.19', 'requests>=2.7.0,<3.0.0']

setup_kwargs = {
    'name': 'perceval-puppet',
    'version': '0.2.3',
    'description': 'Bundle of Perceval backends for Puppet, Inc. ecosystem.',
    'long_description': '# perceval-puppet [![Build Status](https://github.com/chaoss/grimoirelab-perceval-puppet/workflows/tests/badge.svg)](https://github.com/chaoss/grimoirelab-perceval-puppet/actions?query=workflow:tests+branch:master+event:push) [![Coverage Status](https://img.shields.io/coveralls/chaoss/grimoirelab-perceval-puppet.svg)](https://coveralls.io/r/chaoss/grimoirelab-perceval-puppet?branch=master)\n\nBundle of Perceval backends for Puppet ecosystem.\n\n## Backends\n\nThe backends currently managed by this package support the next repositories:\n\n* Puppet Forge\n\n## Requirements\n\nThese set of backends requires Python 3.7 or later, and\n[Perceval](https://github.com/chaoss/grimoirelab-perceval/) to run.\nFor other Python dependencies, please check the `pyproject.toml`\nfile included on this repository.\n\n## Installation\n\nTo install this package you will need to clone the repository first:\n\n```\n$ git clone https://github.com/grimoirelab/perceval-puppet.git\n```\n\nThen you can execute the following commands:\n```\n$ pip3 install -r requirements.txt\n$ pip3 install -e .\n```\n\nIn case you are a developer, you should execute the following commands to install Perceval in your working directory (option `-e`) and the packages of requirements_tests.txt.\n```\n$ pip3 install -r requirements.txt\n$ pip3 install -r requirements_test.txt\n$ pip3 install -e .\n```\n\n## Examples\n\n### Puppet Forge\n\n```\n$ perceval puppetforge\n```\n\n## License\n\nLicensed under GNU General Public License (GPL), version 3 or later.\n',
    'author': 'GrimoireLab Developers',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://chaoss.github.io/grimoirelab/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
