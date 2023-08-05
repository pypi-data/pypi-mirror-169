# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['asyncio_gpsd_client']

package_data = \
{'': ['*']}

install_requires = \
['pydantic>=1.10.2,<2.0.0']

setup_kwargs = {
    'name': 'asyncio-gpsd-client',
    'version': '0.2.0',
    'description': 'asyncio compatible gpsd client',
    'long_description': '# Asycio Gpsd Client\n\n# Install\n\n```shell\npip install asyncio-gpsd-client\n```\n\n# Usage\n\n```python\nimport asyncio\n\nfrom asyncio_gpsd_client import GpsdClient\n\nHOST = "127.0.0.1"\nPORT = 2947\n\n\nasync def main():\n    async with GpsdClient(HOST, PORT) as client:\n        print(await client.poll())  # Get gpsd POLL response\n        while True:\n            print(await client.get_result())  # Get gpsd TPV responses\n\n\nasyncio.run(main())\n```\n',
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
