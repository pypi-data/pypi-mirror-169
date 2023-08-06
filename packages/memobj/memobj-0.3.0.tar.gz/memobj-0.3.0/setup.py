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
    'version': '0.3.0',
    'description': 'A library for defining objects in memory',
    'long_description': '# memobj\nA library for defining objects in memory\n\n## installing\npython 3.11+ only!\n`pip install memobj`\n\n## usage\n```python\nfrom memobj import WindowsProcess, MemoryObject\nfrom memobj.property import *\n\n\n# you can define custom property readers like this\nclass FloatVec3(MemoryProperty):\n    def from_memory(self) -> tuple[float]:\n        # read 3 floats\n        return self.read_formatted_from_offset("fff")\n    \n    def to_memory(self, value: tuple[float]):\n        self.write_formatted_to_offset("fff", value)\n\n\nclass MyObject(MemoryObject):\n    # you can forward reference classes by putting them in a string\n    my_other_object: "MyOtherObject" = ObjectPointer(0x20, "MyOtherObject")\n\n\nclass MyOtherObject(MemoryObject):\n    my_float_vec: tuple[float] = FloatVec3(0x30)\n\n\nprocess = WindowsProcess.from_name("my_process.exe")\n\nmy_object = MyObject(0xFFFFFFFF, process)\nprint(my_object.my_other_object.my_float_vec)\n```\n\n## support\ndiscord\nhttps://discord.gg/7hBStdXkyR\n',
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
