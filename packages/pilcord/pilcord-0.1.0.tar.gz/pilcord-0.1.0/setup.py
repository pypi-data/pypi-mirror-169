# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pilcord']

package_data = \
{'': ['*'], 'pilcord': ['assets/*']}

install_requires = \
['Pillow>=9.2.0,<10.0.0', 'aiohttp>=3.8.1,<4.0.0']

setup_kwargs = {
    'name': 'pilcord',
    'version': '0.1.0',
    'description': 'A library rich with many image generation funcitons powered by PIL for your discord bot such as leveling, welcome card and meme generation!',
    'long_description': None,
    'author': 'Reset',
    'author_email': 'resetwastakenwastaken@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
