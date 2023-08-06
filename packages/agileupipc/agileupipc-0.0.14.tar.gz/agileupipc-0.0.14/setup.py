# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['agileupipc']

package_data = \
{'': ['*']}

install_requires = \
['PyYAML>=5.4.1,<6.0.0',
 'click>=8.1,<9.0',
 'hvac>=1.0.2,<2.0.0',
 'prettytable>=3.3.0,<4.0.0']

entry_points = \
{'console_scripts': ['agileupipc = agileupipc.cli:cli']}

setup_kwargs = {
    'name': 'agileupipc',
    'version': '0.0.14',
    'description': 'Python module to manage AgileUP Informatica PowerCenter.',
    'long_description': '# agileupipc\n\nPython 3.8+ project to manage AgileUP Informatica PowerCenter with the following features:\n\n* Linux and Windows compatible project.\n\n## Prerequisites\n\nThis project uses poetry is a tool for dependency management and packaging in Python. It allows you to declare the \nlibraries your project depends on, it will manage (install/update) them for you. \n\nUse the installer rather than pip [installing-with-the-official-installer](https://python-poetry.org/docs/master/#installing-with-the-official-installer).\n\n```sh\npoetry self add poetry-bumpversion\n```\n\n```sh\npoetry -V\nPoetry (version 1.2.0)\n```\n\n### Windows Path\n\nInstall poetry from powershell in admin mode.\n\n```shell\n(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -\n```\n\nThe path will be `C:\\Users\\<YOURUSER>\\AppData\\Roaming\\Python\\Scripts\\poetry.exe` which will will need to add to your system path.\n\n### Windows GitBash\n\nWhen using gitbash you can setup an alias for the poetry command:\n\n```shell\nalias poetry="\\"C:\\Users\\<YOURUSER>\\AppData\\Roaming\\Python\\Scripts\\poetry.exe\\""\n```\n\n## Getting Started\n\n```sh\npoetry update\n```\n\n```sh\npoetry install\n```\n\n## Run\n```sh\npoetry run agileupipc\n```\n\n## Lint\n```sh\npoetry run flake8\n```\n\n## Test\n```sh\npoetry run pytest\n```\n\n## Publish\n\n* By default we are using [PYPI packages](https://packaging.python.org/en/latest/tutorials/installing-packages/). \n* Create yourself an access token for PYPI and then follow the instructions.\n\n```sh\nexport PYPI_USERNAME=__token__ \nexport PYPI_PASSWORD=<Your API Token>\npoetry publish --build --username $PYPI_USERNAME --password $PYPI_PASSWORD\n```\n\n## Versioning\nWe use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/Agile-Solutions-GB-Ltd/agileup/tags). \n\n## Releasing\n\nWe are using [poetry-bumpversion](https://github.com/monim67/poetry-bumpversion) to manage release versions.\n\n```sh\npoetry version patch\n```\n\n## Dependency\n\nOnce the release has been created it is now available for you to use in other python projects via:\n\n```sh\npip install agileupipc\n```\n\nAnd also for poetry projects via:\n\n```sh\npoetry add agileupipc\n```\n\n## Contributing\n\nPlease read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.\n\n## License\n\nThis project is licensed under the Apache License, Version 2.0 - see the [LICENSE](LICENSE) file for details\n\n\n\n',
    'author': 'agileturret',
    'author_email': 'Paul.Gilligan@agilesolutions.co.uk',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/Agile-Solutions-GB-Ltd/agileupipc',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
