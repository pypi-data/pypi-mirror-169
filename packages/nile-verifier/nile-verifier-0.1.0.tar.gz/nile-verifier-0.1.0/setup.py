# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['nile_verifier']

package_data = \
{'': ['*']}

install_requires = \
['cairo-nile>=0.9.0,<0.10.0',
 'click>=8.1.3,<9.0.0',
 'requests>=2.28.1,<3.0.0',
 'yaspin>=2.2.0,<3.0.0']

entry_points = \
{'nile_plugins': ['verify = nile_verifier.main.verify']}

setup_kwargs = {
    'name': 'nile-verifier',
    'version': '0.1.0',
    'description': 'Nile plugin to verify smart contracts on starkscan.co',
    'long_description': '# Nile verifier plugin\n\nPlugin for [Nile](https://github.com/OpenZeppelin/nile) to verify contracts on [starkscan.co](https://starkscan.co).\n\n> ## ⚠️ WARNING! ⚠️\n>\n> This repo contains highly experimental code.\n> Expect rapid iteration.\n> **Use at your own risk.**\n\n## Installation\n\n1. Install [Poetry](https://python-poetry.org/docs/#installation)\n2. Install dependencies: `poetry install`\n\n## License\n\nMIT\n',
    'author': 'Martín Triay',
    'author_email': 'martriay@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/martriay/nile-verifier-plugin',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
