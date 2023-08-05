# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['digitalearth']

package_data = \
{'': ['*']}

install_requires = \
['cleopatra>=0.2.3,<0.3.0',
 'gdal==3.4.3',
 'loguru>=0.6.0,<0.7.0',
 'matplotlib>=3.5.3,<4.0.0',
 'numpy>=1.23.3,<2.0.0',
 'pyramids-gis>=0.2.5,<0.3.0']

setup_kwargs = {
    'name': 'digitalearth',
    'version': '0.1.5',
    'description': 'Geo-spatial Visualization package',
    'long_description': 'None',
    'author': 'Mostafa Farrag',
    'author_email': 'moah.farag@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<3.12',
}


setup(**setup_kwargs)
