# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['piceimarisconnector', 'piceimarisconnector.test']

package_data = \
{'': ['*'],
 'piceimarisconnector.test': ['.pytest_cache/*', '.pytest_cache/v/cache/*']}

install_requires = \
['numpy>=1.16.6,<2.0.0']

setup_kwargs = {
    'name': 'piceimarisconnector',
    'version': '0.4.2',
    'description': 'IceImarisConnector for python (pIceImarisConnector) is a simple commodity class that eases communication between Bitplane Imaris and python using the Imaris XT interface.',
    'long_description': '# pIceImarisConnector\n\nIceImarisConnector for python (pIceImarisConnector) is a simple commodity class that eases communication between [Bitplane Imaris](http://www.bitplane.com) and [python](http://www.python.org/) using the [Imaris XT interface](http://www.bitplane.com/go/products/imarisxt).\n\n## Documentation\n\n* [API](https://piceimarisconnector.readthedocs.io/en/latest/index.html)\n* [Getting started](https://piceimarisconnector.readthedocs.io/en/latest/usage.html)\n',
    'author': 'Aaron Ponti',
    'author_email': 'aaron.ponti@bsse.ethz.ch',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/aarpon/pIceImarisConnector',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<3.8',
}


setup(**setup_kwargs)
