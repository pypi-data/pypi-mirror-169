# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['freezable']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'freezable',
    'version': '0.1.0',
    'description': 'Freezable mixin class',
    'long_description': None,
    'author': 'Ederic Oytas',
    'author_email': 'edericoytas@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
