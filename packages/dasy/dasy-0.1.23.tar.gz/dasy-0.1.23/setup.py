# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['dasy', 'dasy.builtin', 'dasy.parser']

package_data = \
{'': ['*']}

install_requires = \
['argparse>=1.4.0,<2.0.0',
 'dasy-hy==0.24.1',
 'hyrule>=0.2,<0.3',
 'pytest>=7.1.3,<8.0.0',
 'titanoboa>=0.1.5,<0.2.0',
 'vyper>=0.3.6,<0.4.0']

entry_points = \
{'console_scripts': ['dasy = dasy:main']}

setup_kwargs = {
    'name': 'dasy',
    'version': '0.1.23',
    'description': '',
    'long_description': None,
    'author': 'z80',
    'author_email': 'z80@ophy.xyz',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<3.11',
}


setup(**setup_kwargs)
