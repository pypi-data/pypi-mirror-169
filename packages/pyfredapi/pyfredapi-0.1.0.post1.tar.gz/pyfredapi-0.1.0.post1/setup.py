# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pyfredapi', 'pyfredapi.api']

package_data = \
{'': ['*']}

install_requires = \
['pandas>=1.5.0,<2.0.0', 'pydantic>=1.10.2,<2.0.0', 'requests>=2.28.1,<3.0.0']

setup_kwargs = {
    'name': 'pyfredapi',
    'version': '0.1.0.post1',
    'description': 'A fully featured FRED API client library for Python.',
    'long_description': '# pyfredapi - Python API for the Federal Reserve Economic Data (FRED)\n<!-- badges: start -->\n\n[![PyPi Version](https://img.shields.io/pypi/v/pyfredapi.svg)](https://pypi.python.org/pypi/pyfredapi/)\n[![Supported Python Versions](https://img.shields.io/pypi/pyversions/pyfredapi)](https://pypi.python.org/pypi/pyfredapi)\n[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)\n\n<!-- badges: end -->\n\n`pyfredapi` is a Python API for accessing the [FRED API web service](https://fred.stlouisfed.org/docs/api/fred/) provided by the Federal Reserve Bank of St. Louis. `pyfredapi` makes it easy to retrieve economic data from [FRED](https://fred.stlouisfed.org/) and [ALFRED](https://alfred.stlouisfed.org/). Requests to the api can be customized according to the parameters made available by the web service.\n\n`pyfredapi` aims to be a full featured api for the FRED API web service. `pyfredapi` provides convenient methods for requesting data series, and can return data as a [pandas](https://pandas.pydata.org/) dataframe of as json.\n\n## Installation\n```bash\npip install fredapi\n```\n\n## Basic Usage\n\nBefore using `pyfredapi` and must have a API key to the FRED API web service. You can apply for [one for free](https://fred.stlouisfed.org/docs/api/api_key.html) on the FRED website.\n\nYou can either be set as the environment variable `FRED_API_KEY`, or pass it to the `api_key` parameters when initializing `pyfredapi`.\n\n```python\nfrom pyfredapi import FredApi\n\n# api key set as environment variable\nclient = FredApi()\n\n# api key passed to initializer\nclient = FredApi(api_key = "my_api_key")\n\n# get data for the S&P500\nclient.get_series_data("SP500")\n```\n\n## Documentation\n\nComing soon\n\n## Contributing\n\nComing soon\n',
    'author': 'Greg Moore',
    'author_email': 'gwmoore.career@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<3.11',
}


setup(**setup_kwargs)
