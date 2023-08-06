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
    'version': '0.2.0',
    'description': 'A library for defining objects in memory',
    'long_description': '# memobj\nA library for defining objects in memory\n\n## installing\npython 3.11+ only!\n`pip install memobj`\n\n## support\ndiscord\nhttps://discord.gg/7hBStdXkyR\n',
    'author': 'StarrFox',
    'author_email': 'starrfox6312@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/StarrFox/memobj',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.11,<4.0',
}


setup(**setup_kwargs)
