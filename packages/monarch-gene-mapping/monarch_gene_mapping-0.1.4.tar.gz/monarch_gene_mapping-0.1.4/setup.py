# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['monarch_gene_mapping']

package_data = \
{'': ['*']}

install_requires = \
['click==8.0.4',
 'ipython>=8.5.0,<9.0.0',
 'kghub-downloader>=0.1.14,<0.2.0',
 'pandas>=1.4.2,<2.0.0',
 'typer==0.4']

entry_points = \
{'console_scripts': ['gene-mapping = monarch_gene_mapping.main:typer_app']}

setup_kwargs = {
    'name': 'monarch-gene-mapping',
    'version': '0.1.4',
    'description': 'Project for mapping source namespaces to preffered namespaces in Monarch Initiative',
    'long_description': 'None',
    'author': 'Tim Putman',
    'author_email': 'putmantime@users.noreply.github.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
