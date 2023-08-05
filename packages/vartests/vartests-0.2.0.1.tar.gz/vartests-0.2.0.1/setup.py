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
    'version': '0.2.0.1',
    'description': 'Statistic tests for Value at Risk (VaR) Models.',
    'long_description': '<!-- buttons -->\n<p align="center">\n    <a href="https://www.python.org/">\n        <img src="https://img.shields.io/badge/python-v3-brightgreen.svg"\n            alt="python"></a> &nbsp;\n    <a href="https://opensource.org/licenses/MIT">\n        <img src="https://img.shields.io/badge/license-MIT-brightgreen.svg"\n            alt="MIT license"></a> &nbsp;\n    <a href="https://github.com/psf/black">\n        <img src="https://img.shields.io/badge/code%20style-black-000000.svg"\n            alt="Code style: black"></a> &nbsp;\n    <a href="http://mypy-lang.org/">\n        <img src="http://www.mypy-lang.org/static/mypy_badge.svg"\n            alt="Checked with mypy"></a> &nbsp;\n</p>\n\n<!-- content -->\n\n**vartests** is a Python library to perform some statistical tests to evaluate Value at Risk (VaR) Models, such as:\n\n- **T-test**: verify if mean of distribution is zero;\n- **Kupiec Test (1995)**: verify if the number of violations is consistent with the violations predicted by the model;\n- **Berkowitz Test (2001)**: verify if conditional distributions of returns "GARCH(1,1)"  used in the VaR Model is adherent to the data. In this specific test, we do not observe the whole data, only the tail;\n- **Christoffersen and Pelletier Test (2004)**: also known as Duration Test. Duration is time between violations of VaR. It tests if VaR Model has quickly response to market movements by consequence the violations do not form volatility clusters. This test verifies if violations has no memory i.e. should be independent.\n\n## Installation\n\n### Using pip\n\nYou can install using the pip package manager by running:\n\n```sh\npip install vartests\n```\n\nAlternatively, you could install the latest version directly from Github:\n\n```sh\npip install https://github.com/rafa-rod/vartests/archive/refs/heads/main.zip\n```\n\n## Why vartests is important?\n\nAfter VaR calculation, it is necessary to perform statistic tests to evaluate the VaR Models. To select the best model, they should be validated by backtests.\n\n## Example\n\nFirst of all, lets read a file with a PnL (distribution of profit and loss) of a portfolio in which also contains the VaR and its violations.\n\n```python\nimport pandas as pd\n\ndata = pd.read_excel("Example.xlsx", index_col=0)\nviolations = data["Violations"]\npnl = data["PnL"] \ndata.sample(5)\n```\n\nThe dataframe looks like:\n\n```\n\' |     PnL       |      VaR        |   Violations |\n  | -889.003707   | -2554.503872    |            0 |\n  | -2554.503872  | -2202.221691    |            1 | \n  | -887.527423   | -2193.692570    |            0 |  \n  | -274.344126   | -2160.290746    |            0 | \n  | 1376.018638   | -5719.833100    |            0 |\'\n```\n\nNot all tests should be applied to the VaR Model. Some of them should be applied when the VaR Model has the assumption of zero mean or follow a specific distribution.\n\n```python\nimport vartests\n\nvartests.zero_mean_test(pnl.values, conf_level=0.95)\n```\n\nThis assumption is commonly used in parametric VaR like EWMA and GARCH Models. Besides that, is necessary check assumption of the distribution. So you should test with Berkowitz (2001):\n\n```python\nimport vartests\n\nvartests.berkowtiz_tail_test(pnl, volatility_window=252, var_conf_level=0.99, conf_level=0.95)\n```\n\nThe following tests should be used to any kind of VaR Models.\n\n```python\nimport vartests\n\nvartests.kupiec_test(violations, var_conf_level=0.99, conf_level=0.95)\n\nvartests.duration_test(violations, conf_level=0.95)\n```\n\nIf you want to see the failure ratio of the VaR Model, just type:\n\n```python\nimport vartests\n\nvartests.failure_rate(violations)\n```',
    'author': 'Rafael Rodrigues',
    'author_email': 'rafael.rafarod@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/rafa-rod/vartests.git',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
