# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pyramids']

package_data = \
{'': ['*']}

install_requires = \
['Fiona==1.8.21',
 'GDAL==3.4.3',
 'Rtree>=1.0.0,<2.0.0',
 'Shapely>=1.8.4,<2.0.0',
 'affine>=2.3.1,<3.0.0',
 'geopandas>=0.11.1,<0.12.0',
 'geopy>=2.2.0,<3.0.0',
 'loguru>=0.6.0,<0.7.0',
 'matplotlib>=3.5.3,<4.0.0',
 'netCDF4>=1.6.1,<2.0.0',
 'pandas>=1.4.4,<2.0.0',
 'pyproj>=3.4.0,<4.0.0',
 'rasterio>=1.3.0,<2.0.0']

setup_kwargs = {
    'name': 'pyramids-gis',
    'version': '0.2.5',
    'description': 'GIS utility package',
    'long_description': 'None',
    'author': 'Mostafa Farrag',
    'author_email': 'moah.farag@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/MAfarrag/pyramids',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<3.12',
}


setup(**setup_kwargs)
