# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['easyuri']

package_data = \
{'': ['*']}

install_requires = \
['hstspreload>=2022.9.1,<2023.0.0', 'requests>=2.28.1,<3.0.0']

setup_kwargs = {
    'name': 'easyuri',
    'version': '0.0.5',
    'description': 'an intelligent URI interface',
    'long_description': '',
    'author': 'Angelo Gladding',
    'author_email': 'angelo@ragt.ag',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<3.11',
}


setup(**setup_kwargs)
