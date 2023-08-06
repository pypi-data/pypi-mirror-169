# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['strprofiler']
install_requires = \
['numpy>=1.23.3,<2.0.0',
 'openpyxl>=3.0.10,<4.0.0',
 'pandas>=1.4.3,<2.0.0',
 'rich-click>=1.5.2,<2.0.0']

entry_points = \
{'console_scripts': ['strprofiler = strprofiler:strprofiler']}

setup_kwargs = {
    'name': 'strprofiler',
    'version': '0.1.0',
    'description': 'A simple python utility to compare short tandem repeat (STR) profiles.',
    'long_description': None,
    'author': 'Jared Andrews',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/j-andrews7/strprofiler',
    'py_modules': modules,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
