# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['freezable']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'freezable',
    'version': '0.1.1',
    'description': 'Freezable mixin class',
    'long_description': '# `freezable` - Freezable objects in Python\n\nNOTICE: This project is in Alpha. Code may be unstable. API is subject to\nchange.\n\nThis Python package provides a mixin class to implement "freezable" objects.\nWhen an object is frozen, the data contained within the object is marked as\nimmutable.\n\n\n## Installation\n\n```\npip install freezable\n```\n\n## Basic Usage\n\n`freezable` provides the `Freezable` mixin class for user-defined objects:\n\n```python\nfrom freezable import Freezable\n\nclass SomeFreezable(Freezable):\n    ...\n```\n\n**You do not need to call __init__ for this class;** you only need to subclass\nit, even in multiple inheritance.\n\nTo freeze an freezable object, use the `freeze()` method, and to unfreeze, use\nthe `unfreeze()` method. You can check if a freezable object is frozen using\nthe `is_frozen()` method.\n\n```python\nobj = SomeFreezable()\n\nassert not obj.is_frozen()\n\nobj.freeze()\nassert obj.is_frozen()\n\nobj.unfreeze()\nassert not obj.is_frozen()\n```\n\nWhile an object is frozen, setting and deleting attributes of that object\nis disabled; these operations raise a `FrozenError` while it is frozen.\n\n```python\nobj = SomeFreezable()\nobj.freeze()\n\n# Both of these operations will raise a FrozenError:\nobj.attr = 5\ndel obj.attr\n```\n\nIf you don\'t want this behavior, you can override the special methods in the\nclass body:\n```python\n__setattr__ = object.__setattr__\n__delattr__ = object.__delattr__\n```\n\nThe package also provides the `@enabled_when_unfrozen` instance method\ndecorator only enables a method if the object is unfrozen; when it is frozen,\nit raises a `FrozenError`. Make sure to only use this decorator in a class\nthat subclasses `Freezable`.\n\n```python\nclass SomeFreezable(Freezable):\n    @enabled_when_unfrozen\n    def some_mutating_method(self):\n        ...\n```\n',
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
