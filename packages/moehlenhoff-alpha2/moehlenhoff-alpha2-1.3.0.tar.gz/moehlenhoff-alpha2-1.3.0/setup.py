# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['moehlenhoff_alpha2']

package_data = \
{'': ['*']}

install_requires = \
['aiohttp', 'xmltodict']

setup_kwargs = {
    'name': 'moehlenhoff-alpha2',
    'version': '1.3.0',
    'description': 'Python client for the Moehlenhoff Alpha2 underfloor heating system',
    'long_description': '# python-moehlenhoff-alpha2\nPython client for the Moehlenhoff Alpha2 underfloor heating system\n\n## Vendor documentation\n- https://www.ezr-portal.de/backend/documents.php?d=Alpha2_XML_Schnittstellen_Informationen.zip\n\n## Installation\n\nMoehlenhoff Alpha2 can be installed from PyPI using `pip` or your package manager of choice:\n\n``` bash\npip install moehlenhoff-alpha2\n```\n\n## Usage example\n\n``` python\nimport asyncio\nfrom moehlenhoff_alpha2 import Alpha2Base\n\nasync def main():\n    base = Alpha2Base("192.168.1.1")\n    await base.update_data()\n    # Set current date and time in base\n    await base.set_datetime()\n    # Increase the temperature of heatarea by 0.2 degrees\n    heat_area = list(base.heat_areas)[0]\n    t_target = heat_area["T_TARGET"] + 0.2\n    await base.update_heat_area(heat_area["ID"], {"T_TARGET": t_target})\n\nasyncio.run(main())\n```\n\n## Development\nGet [Python Poetry](https://python-poetry.org/docs/)\n```\n# Install project dependencies\npoetry install\n\n# Run tests\nALPHA2_BASE_ADDRESS=<address> poetry run pytest --tb=short -o junit_family=xunit2 --junitxml=testreport.xml --cov-append --cov moehlenhoff_alpha2 --cov-report term --cov-report xml -v tests\n```\n',
    'author': 'Jan Schneider',
    'author_email': 'oss@janschneider.net',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/j-a-n/python-moehlenhoff-alpha2',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
