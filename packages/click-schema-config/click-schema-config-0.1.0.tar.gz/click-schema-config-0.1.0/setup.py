# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['click_schema_config']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.1.3,<9.0.0']

setup_kwargs = {
    'name': 'click-schema-config',
    'version': '0.1.0',
    'description': '',
    'long_description': '',
    'author': 'Joy Void Joy',
    'author_email': 'joy.void.joy@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
