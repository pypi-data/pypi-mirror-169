# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['eotds']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'eotds',
    'version': '0.1.0',
    'description': 'Earth Observation Training Datasets',
    'long_description': '# EOTDS\n\nMain python library\n',
    'author': 'Juan Sensio',
    'author_email': 'it@earthpulse.es',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
