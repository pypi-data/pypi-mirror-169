# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['vartests']

package_data = \
{'': ['*']}

install_requires = \
['arch>=5.0.1,<6.0.0',
 'pandas>=1.3.4,<2.0.0',
 'pygosolnp>=2021.5.1,<2022.0.0',
 'statsmodels>=0.13.2,<0.14.0',
 'tqdm>=4.62.3,<5.0.0']

setup_kwargs = {
    'name': 'vartests',
    'version': '0.1.17',
    'description': 'Statistic tests for Value at Risk (VaR) Models.',
    'long_description': 'None',
    'author': 'Rafael Rodrigues',
    'author_email': 'rafael.rafarod@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
