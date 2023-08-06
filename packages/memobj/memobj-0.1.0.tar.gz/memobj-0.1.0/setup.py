# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['memobj']

package_data = \
{'': ['*']}

install_requires = \
['regex>=2022.9.13,<2023.0.0']

setup_kwargs = {
    'name': 'memobj',
    'version': '0.1.0',
    'description': '',
    'long_description': 'None',
    'author': 'StarrFox',
    'author_email': 'starrfox6312@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.11,<4.0',
}


setup(**setup_kwargs)
