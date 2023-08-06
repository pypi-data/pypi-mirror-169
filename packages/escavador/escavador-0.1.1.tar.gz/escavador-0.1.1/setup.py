# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['escavador', 'escavador.resources', 'escavador.resources.helpers']

package_data = \
{'': ['*']}

install_requires = \
['aiodns>=3.0.0,<4.0.0',
 'asyncio>=3.4.3,<4.0.0',
 'cchardet>=2.1.7,<3.0.0',
 'python-dotenv>=0.19.2,<0.20.0',
 'requests>=2.27.1,<3.0.0']

setup_kwargs = {
    'name': 'escavador',
    'version': '0.1.1',
    'description': 'A library to  interact with Escavador API',
    'long_description': 'None',
    'author': 'Your Name',
    'author_email': 'you@example.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
