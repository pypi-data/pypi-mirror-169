# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['minus_k']
setup_kwargs = {
    'name': 'minus-k',
    'version': '0.0.1',
    'description': '',
    'long_description': 'from minus_K import *\nminus_K()',
    'author': 'Shokhrukh Shavkatov',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'py_modules': modules,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
