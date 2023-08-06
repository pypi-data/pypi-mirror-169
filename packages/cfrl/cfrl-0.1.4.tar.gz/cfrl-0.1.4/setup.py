# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['cfrl',
 'cfrl.agents',
 'cfrl.experiments',
 'cfrl.nn',
 'cfrl.optimizers',
 'cfrl.policies',
 'cfrl.utils',
 'cfrl.wrappers']

package_data = \
{'': ['*']}

install_requires = \
['gym[classic_control]>=0.23.0,<0.24.0',
 'numpy>=1.10.4,<2.0.0',
 'opencv-python>=3.4.0,<4.0.0',
 'packaging>=21.3,<22.0',
 'torch==1.12.0',
 'wandb>=0.13.3,<0.14.0']

extras_require = \
{'atari': ['ale-py>=0.7,<0.8', 'AutoROM[accept-rom-license]>=0.4.2,<0.5.0']}

setup_kwargs = {
    'name': 'cfrl',
    'version': '0.1.4',
    'description': '',
    'long_description': '',
    'author': 'Chufan Chen',
    'author_email': 'chenchufan@zju.edu.cn',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
