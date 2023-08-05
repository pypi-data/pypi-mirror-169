# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['earth2observe', 'earth2observe.gee']

package_data = \
{'': ['*']}

install_requires = \
['Fiona==1.8.21',
 'earthengine-api>=0.1.324,<0.2.0',
 'ecmwf-api-client>=1.6.3,<2.0.0',
 'gdal==3.4.3',
 'loguru>=0.6.0,<0.7.0',
 'netCDF4>=1.6.1,<2.0.0',
 'numpy>=1.23.3,<2.0.0',
 'pandas>=1.4.4,<2.0.0',
 'pyramids-gis>=0.2.4,<0.3.0']

setup_kwargs = {
    'name': 'earth2observe',
    'version': '0.1.3',
    'description': 'remote sensing package',
    'long_description': 'None',
    'author': 'Mostafa Farrag',
    'author_email': 'moah.farag@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/MAfarrag/earth2observe',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
