# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['retracto']

package_data = \
{'': ['*']}

install_requires = \
['cohere>=2.4.2,<3.0.0',
 'google-api-python-client>=2.62.0,<3.0.0',
 'google-auth-oauthlib>=0.5.3,<0.6.0',
 'python-dotenv>=0.21.0,<0.22.0',
 'requests>=2.28.1,<3.0.0',
 'typer[all]>=0.6.1,<0.7.0']

entry_points = \
{'console_scripts': ['retracto = retracto.app:app']}

setup_kwargs = {
    'name': 'retracto',
    'version': '1.0.0',
    'description': '',
    'long_description': 'None',
    'author': 'Amit Krishna A',
    'author_email': 'amit.ananthkumar@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
