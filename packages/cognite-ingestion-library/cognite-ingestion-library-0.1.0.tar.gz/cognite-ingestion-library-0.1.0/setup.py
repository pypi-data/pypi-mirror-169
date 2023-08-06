# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': '.'}

packages = \
['cognite', 'cognite.ingestion']

package_data = \
{'': ['*']}

install_requires = \
['cognite-sdk>=4.5.4,<5.0.0',
 'dacite>=1.6.0,<2.0.0',
 'decorator>=5.1.1,<6.0.0',
 'pyjq>=2.6,<3.0',
 'python-dateutil>=2.8.2,<3.0.0']

setup_kwargs = {
    'name': 'cognite-ingestion-library',
    'version': '0.1.0',
    'description': 'Library for converting arbitrary schema output to CDF types and ingesting them',
    'long_description': 'None',
    'author': 'Einar Omang',
    'author_email': 'einar.omang@cognite.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
