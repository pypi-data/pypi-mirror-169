# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['balcony']

package_data = \
{'': ['*']}

install_requires = \
['boto3>=1.24.80,<2.0.0',
 'inflect>=6.0.0,<7.0.0',
 'jmespath>=1.0.1,<2.0.0',
 'rich>=12.5.1,<13.0.0',
 'termcolor>=2.0.1,<3.0.0',
 'typer>=0.6.1,<0.7.0']

entry_points = \
{'console_scripts': ['balcony = balcony.cli:run_app']}

setup_kwargs = {
    'name': 'arzuhal',
    'version': '0.0.13',
    'description': 'No description',
    'long_description': '# arzuhal',
    'author': 'Oguzhan Yilmaz',
    'author_email': 'oguzhanylmz271@gmail.com',
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
