# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['demoi123123123123']

package_data = \
{'': ['*']}

install_requires = \
['Django>=4.1.1,<5.0.0', 'pandas==1.0.0']

setup_kwargs = {
    'name': 'demoi123123123123',
    'version': '0.1.0',
    'description': '',
    'long_description': '',
    'author': 'Evgeny Pistun',
    'author_email': 'Evgeny.Pistun@kaspersky.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
