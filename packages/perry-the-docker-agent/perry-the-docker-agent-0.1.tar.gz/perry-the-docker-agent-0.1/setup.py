# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['perry_the_docker_agent']

package_data = \
{'': ['*'],
 'perry_the_docker_agent': ['sceptre/config/dev/*', 'sceptre/templates/*']}

install_requires = \
['PyYAML==5.4.1',
 'boto3==1.24.80',
 'click>=7.1.1,<7.2.0',
 'colorlog>=6.7.0,<7.0.0',
 'pathspec>=0.10.1,<0.11.0',
 'pydantic>=1.10.2,<2.0.0',
 'sceptre>=3.2.0,<4.0.0',
 'typer[all]>=0.6.1,<0.7.0']

entry_points = \
{'console_scripts': ['perry = perry_the_docker_agent:main.app']}

setup_kwargs = {
    'name': 'perry-the-docker-agent',
    'version': '0.1',
    'description': 'Your cool remote docker agent in the cloud',
    'long_description': None,
    'author': 'Daverin',
    'author_email': 'mail@daverin.net',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
