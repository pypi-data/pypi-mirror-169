# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['sanctum']

package_data = \
{'': ['*']}

modules = \
['LICENSE']
install_requires = \
['aiohttp>=3.6.0,<4.0.0']

setup_kwargs = {
    'name': 'sanctum-tc',
    'version': '0.6.0a1',
    'description': 'Library for interacting with the Sanctum API',
    'long_description': 'None',
    'author': 'LightSage',
    'author_email': 'lightsage01@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'py_modules': modules,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
