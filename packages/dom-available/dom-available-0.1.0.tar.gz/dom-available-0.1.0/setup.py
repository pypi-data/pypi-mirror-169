# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['available']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'dom-available',
    'version': '0.1.0',
    'description': '',
    'long_description': '',
    'author': 'Aman Jha',
    'author_email': 'amanjha22@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
