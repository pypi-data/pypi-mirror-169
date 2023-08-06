# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pytorch_tao']

package_data = \
{'': ['*'], 'pytorch_tao': ['templates/*']}

install_requires = \
['GitPython>=3.1.27,<4.0.0',
 'Jinja2>=3.1.2,<4.0.0',
 'PyYAML>=6.0,<7.0',
 'click>=8.1.3,<9.0.0',
 'kaggle>=1.5.12,<2.0.0',
 'optuna>=3.0.2,<4.0.0',
 'torch>=1.12.1,<2.0.0']

entry_points = \
{'console_scripts': ['tao = pytorch_tao.cli:main',
                     'tao_devtool = pytorch_tao.devtool:main']}

setup_kwargs = {
    'name': 'pytorch-tao',
    'version': '0.1.5',
    'description': 'Tao for PyTorch',
    'long_description': 'None',
    'author': 'chenglu',
    'author_email': 'chenglu.she@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<3.10',
}


setup(**setup_kwargs)
