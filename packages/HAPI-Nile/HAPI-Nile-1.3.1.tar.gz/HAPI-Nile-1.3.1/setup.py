# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['Hapi', 'Hapi.hm', 'Hapi.plot', 'Hapi.rrm']

package_data = \
{'': ['*'], 'Hapi': ['parameters/.gitignore']}

install_requires = \
['Fiona==1.8.21',
 'GDAL==3.4.3',
 'Oasis-Optimization>=1.0.2,<2.0.0',
 'cleopatra>=0.2.3,<0.3.0',
 'digitalearth>=0.1.5,<0.2.0',
 'geopandas>=0.11.1,<0.12.0',
 'geostatista>=0.1.2,<0.2.0',
 'loguru>=0.6.0,<0.7.0',
 'matplotlib>=3.5.3,<4.0.0',
 'pandas>=1.4.4,<2.0.0',
 'pyramids-gis>=0.2.5,<0.3.0',
 'rasterio>=1.3.2,<2.0.0',
 'rasterstats>=0.17.0,<0.18.0',
 'requests>=2.28.1,<3.0.0',
 'scipy>=1.9.1,<2.0.0',
 'statista>=0.1.6,<0.2.0',
 'statsmodels>=0.13.2,<0.14.0']

setup_kwargs = {
    'name': 'hapi-nile',
    'version': '1.3.1',
    'description': 'Distributed Hydrological and Hydrodynamic model',
    'long_description': 'None',
    'author': 'Mostafa Farrag',
    'author_email': 'moah.farag@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/MAfarrag/Hapi',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<3.12',
}


setup(**setup_kwargs)
