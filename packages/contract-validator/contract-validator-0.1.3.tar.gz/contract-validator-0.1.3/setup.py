# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['contract_validator']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'contract-validator',
    'version': '0.1.3',
    'description': 'Validador de contrato baseado no JsonSchema',
    'long_description': '',
    'author': 'Victor Magdalene',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
