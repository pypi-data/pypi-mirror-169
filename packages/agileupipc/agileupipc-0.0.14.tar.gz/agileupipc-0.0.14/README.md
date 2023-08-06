# agileupipc

Python 3.8+ project to manage AgileUP Informatica PowerCenter with the following features:

* Linux and Windows compatible project.

## Prerequisites

This project uses poetry is a tool for dependency management and packaging in Python. It allows you to declare the 
libraries your project depends on, it will manage (install/update) them for you. 

Use the installer rather than pip [installing-with-the-official-installer](https://python-poetry.org/docs/master/#installing-with-the-official-installer).

```sh
poetry self add poetry-bumpversion
```

```sh
poetry -V
Poetry (version 1.2.0)
```

### Windows Path

Install poetry from powershell in admin mode.

```shell
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -
```

The path will be `C:\Users\<YOURUSER>\AppData\Roaming\Python\Scripts\poetry.exe` which will will need to add to your system path.

### Windows GitBash

When using gitbash you can setup an alias for the poetry command:

```shell
alias poetry="\"C:\Users\<YOURUSER>\AppData\Roaming\Python\Scripts\poetry.exe\""
```

## Getting Started

```sh
poetry update
```

```sh
poetry install
```

## Run
```sh
poetry run agileupipc
```

## Lint
```sh
poetry run flake8
```

## Test
```sh
poetry run pytest
```

## Publish

* By default we are using [PYPI packages](https://packaging.python.org/en/latest/tutorials/installing-packages/). 
* Create yourself an access token for PYPI and then follow the instructions.

```sh
export PYPI_USERNAME=__token__ 
export PYPI_PASSWORD=<Your API Token>
poetry publish --build --username $PYPI_USERNAME --password $PYPI_PASSWORD
```

## Versioning
We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/Agile-Solutions-GB-Ltd/agileup/tags). 

## Releasing

We are using [poetry-bumpversion](https://github.com/monim67/poetry-bumpversion) to manage release versions.

```sh
poetry version patch
```

## Dependency

Once the release has been created it is now available for you to use in other python projects via:

```sh
pip install agileupipc
```

And also for poetry projects via:

```sh
poetry add agileupipc
```

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

## License

This project is licensed under the Apache License, Version 2.0 - see the [LICENSE](LICENSE) file for details



