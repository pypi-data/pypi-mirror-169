# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['loaderinsta']
setup_kwargs = {
    'name': 'loaderinsta',
    'version': '0.0.1',
    'description': 'Instagram post yuklash',
    'long_description': '',
    'author': 'Brodyaga',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'py_modules': modules,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
