# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['ibm_wmla_client', 'ibm_wmla_client.assets']

package_data = \
{'': ['*']}

install_requires = \
['ibm-cloud-sdk-core>=3.15.3,<4.0.0',
 'ibm-wmla>=0.1.0,<0.2.0',
 'python_dateutil>=2.5.3,<3.0.0',
 'requests>=2.20,<3.0']

setup_kwargs = {
    'name': 'ibm-wmla-client',
    'version': '0.1.1',
    'description': 'A python based client to simplify using Watson Machine Learning Accelerator',
    'long_description': 'Welcom to ``ibm-wmla-client``\n-------------------------------\n\n``ibm-wmla-client`` is a python based client to simplify using Watson Machine Learning Accelerator Elastic Distributed Inference (WMLA EDI).\n\nPrerequisites\n--------------------\n+ Python 3.5.3 or above\n+ `ibm_wmla`_ 0.1.0 or above\n\n.. _ibm_wmla: https://pypi.org/project/ibm-wmla/\n\n',
    'author': 'Shuang Yu',
    'author_email': 'shuang.yu@ibm.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/sherryyyu/ibm-wmla-python-client',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
