# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['data_minion', 'data_minion.resources']

package_data = \
{'': ['*']}

install_requires = \
['BeautifulSoup4>=4.9.3,<5.0.0',
 'PySimpleGUIQt>=0.35.0,<0.36.0',
 'helium>=3.0.8,<4.0.0',
 'openpyxl>=3.0.10,<4.0.0']

setup_kwargs = {
    'name': 'data-minion',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'David Flood',
    'author_email': 'davidfloodii@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
