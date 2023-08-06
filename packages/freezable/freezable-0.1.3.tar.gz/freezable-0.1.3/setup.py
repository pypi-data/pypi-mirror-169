# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['freezable']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'freezable',
    'version': '0.1.3',
    'description': 'Dynamically immutable objects',
    'long_description': '<a href="https://badge.fury.io/py/freezable"><img src="https://badge.fury.io/py/freezable.svg" alt="PyPI version" height="18"></a>\n<a href=\'https://python-freezable.readthedocs.io/en/latest/?badge=latest\'>\n    <img src=\'https://readthedocs.org/projects/python-freezable/badge/?version=latest\' alt=\'Documentation Status\' />\n</a>\n<a href="https://github.com/ederic-oytas/python-freezable/blob/main/LICENSE"><img alt="GitHub license" src="https://img.shields.io/github/license/ederic-oytas/python-freezable"></a>\n\n# Freezable: Dynamically Immutable Objects\n\n> NOTICE: This project is in Alpha; expect bugs! API is also subject to\n  change.\n  \nFreezable is a package that allows you to implement "freezable" types in\nPython, which can either be "frozen" or "unfrozen." When frozen, all operations\nand methods that mutate the object are disabled.\n\nHere is one example:\n```python\nfrom freezable import Freezable, FrozenError, enabled_when_unfrozen\n\nclass FreezableStack(Freezable):\n    \n    def __init__(self):\n        self._data = []\n    \n    @enabled_when_unfrozen\n    def push(self, x):\n        self._data.append(x)\n\n    def top(self):\n        return self._data[-1] if self._data else None\n\nstk = FreezableStack()\nassert stk.top() is None\n\nstk.push(1)\nassert stk.top() == 1\nstk.push(2)\nassert stk.top() == 2\n\nstk.freeze()\n\ntry:\n    stk.push(3)  # error because stk is frozen\nexcept FrozenError:\n    pass\n\nassert stk.top() == 2  # operation did not proceed\n\nstk.unfreeze()\nstk.push(3)\nassert stk.top() == 3\n```\n\nThis package can be useful in finding logical errors in which objects are\nmutated when they are not supposed to.\n\nSee the [documentation][1] for more information on how to use this project.\n\n## Links\n\n[Documentation @ReadTheDocs][1]\n\n[PyPI Link](https://pypi.org/project/freezable/)\n\n## Installation\n\nThis package can be installed using Pip:\n```\npip install freezable\n```\n\n[1]: https://python-freezable.readthedocs.io\n',
    'author': 'Ederic Oytas',
    'author_email': 'edericoytas@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/ederic-oytas/python-freezable',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
