# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['resqml22']

package_data = \
{'': ['*']}

install_requires = \
['coverage[toml]>=6.2,<7.0', 'xsdata[cli]>=22.9,<23.0']

setup_kwargs = {
    'name': 'resqml22',
    'version': '1.0.0',
    'description': 'Energyml types',
    'long_description': 'Energyml types\n==============\n\n[![License](https://img.shields.io/pypi/l/resqml22py)](https://github.com/geosiris-technologies/energyml-python-generator/blob/main/LICENSE)\n[![Documentation Status](https://readthedocs.org/projects/energyml-python-generator/badge/?version=latest)](https://energyml-python-generator.readthedocs.io/en/latest/?badge=latest)\n![Python version](https://img.shields.io/pypi/pyversions/resqml22py)\n![Status](https://img.shields.io/pypi/status/resqml22py)\n\n\n\n\nInstallation\n------------\n\nEnergyml-types can be installed with pip : \n\n```console\npip install resqml22\n```\n\nor with poetry: \n```console\npoetry add resqml22\n```\n',
    'author': 'Valentin Gauthier',
    'author_email': 'valentin.gauthier@geosiris.com',
    'maintainer': 'Lionel Untereiner',
    'maintainer_email': 'lionel.untereiner@geosiris.com',
    'url': 'http://www.geosiris.com',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
