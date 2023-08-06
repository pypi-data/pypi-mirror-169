# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['gophient']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'gophient',
    'version': '1.1.0',
    'description': 'Client library for the Gopherspace',
    'long_description': None,
    'author': 'Arisu W.',
    'author_email': 'arisuchr@riseup.net',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
