# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['gpsd_client']

package_data = \
{'': ['*']}

install_requires = \
['pydantic>=1.10.2,<2.0.0']

setup_kwargs = {
    'name': 'asyncio-gpsd-client',
    'version': '0.1.0',
    'description': 'asyncio compatible gpsd client',
    'long_description': '',
    'author': 'Zachary Juang',
    'author_email': 'zachary822@me.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
