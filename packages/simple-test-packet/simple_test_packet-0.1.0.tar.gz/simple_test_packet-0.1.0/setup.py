# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['simple_test_packet']

package_data = \
{'': ['*']}

install_requires = \
['fastapi>=0.85.0,<0.86.0', 'uvicorn>=0.18.3,<0.19.0']

setup_kwargs = {
    'name': 'simple-test-packet',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'Dima Abramovich',
    'author_email': 'abramovich_d@rocketdata.io',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/rofar91/simple-test-packet',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
