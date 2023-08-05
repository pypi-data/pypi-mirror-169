# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['honeywell_imtcc_poller',
 'honeywell_imtcc_poller.gateways',
 'honeywell_imtcc_poller.models']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.1.3,<9.0.0',
 'prometheus-client>=0.14.1,<0.15.0',
 'requests>=2.28.1,<3.0.0',
 'tenacity>=8.0.1,<9.0.0']

entry_points = \
{'console_scripts': ['poll-honeywell = honeywell_imtcc_poller:run_cli']}

setup_kwargs = {
    'name': 'honeywell-imtcc-poller',
    'version': '0.5.0',
    'description': 'Tool for logging stats from the Honeywell international.mytotalconnectcomfort.com site',
    'long_description': '# Honeywell IMTCC Poller\n\nTool for polling heating data from [Honeywell International My Total Connect Comfort](https://international.mytotalconnectcomfort.com/Account/Login), combining it with the outside temperature from the [OpenWeather API](https://openweathermap.org/current) and presenting them as [Prometheus](https://prometheus.io/) metrics.\n\n## Installation\n\nThis is not yet packaged. To run, you will need to clone the repo with `git` and install the required prerequisites:\n\n* [Python 3.10.4](https://www.python.org/downloads/) or above\n* [Poetry 1.2.0](https://python-poetry.org/docs/#installation) or above\n\nYou can then run `poetry install` to install the required python libraries.\n\n## Usage\n\nCreate environment variables containing your Honeywell [login credetials](https://international.mytotalconnectcomfort.com/Account/Login):\n\n```bash\n$ export HONEYWELL_EMAIL_ADDRESS="foo@example.com"\n$ export HONEYWELL_PASSWORD="ThisIsNotARealPassword"\n```\n\nCreate environment variables containing your OpenWeather [API key](https://home.openweathermap.org/api_keys) and co-ordinates for where you want the outside temperature to reflect:\n\n```bash\n$ export OPENWEATHER_API_KEY="foo-openweather-api-key"\n$ export OPENWEATHER_LATITUDE="51.476852"\n$ export OPENWEATHER_LONGITUDE="0.0005"\n```\n\nYou can then run the tool via poetry:\n\n```bash\n$ poetry run poll-honeywell\nKitchen: 20.0\nHarrys Room: 20.5\nLounge: 19.5\nMain Bedroom: 19.5\nHot Water: 48.0\nOutside: 16.36\n```\n\nThe tool will authenticate with the Honeywell API using the login credentials supplied. It will make the calls every 60 seconds in order to get location and zone data.\n\nThe Prometheus metrics are made available for scraping on `https://localhost:8000` while the tool is running.\n\n## Limitations\n\n- Assumes you have zero or one hot water systems\n- Limited error handling\n\n## Developing\n\nRunning tests:\n\n```bash\n$ make test\n```\n## License\n\nThis project is licensed under the terms of the [MIT License](./LICENSE.md).\n',
    'author': 'Dave Randall',
    'author_email': '19395688+daveygit2050@users.noreply.github.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
