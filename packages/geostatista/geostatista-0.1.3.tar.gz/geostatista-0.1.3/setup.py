# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['geostatista']

package_data = \
{'': ['*']}

install_requires = \
['Fiona==1.8.21',
 'GDAL==3.4.3',
 'loguru>=0.6.0,<0.7.0',
 'matplotlib>=3.5.3,<4.0.0',
 'pandas>=1.4.4,<2.0.0',
 'pyramids-gis>=0.2.5,<0.3.0',
 'statista>=0.1.6,<0.2.0']

setup_kwargs = {
    'name': 'geostatista',
    'version': '0.1.3',
    'description': 'statistics package',
    'long_description': 'None',
    'author': 'Mostafa Farrag',
    'author_email': 'moah.farag@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/MAfarrag/geostatista',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>3.9,<3.12',
}


setup(**setup_kwargs)
