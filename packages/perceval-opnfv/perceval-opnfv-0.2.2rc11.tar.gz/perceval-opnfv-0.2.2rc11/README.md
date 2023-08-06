# perceval-opnfv [![Build Status](https://github.com/chaoss/grimoirelab-perceval-opnfv/workflows/tests/badge.svg)](https://github.com/chaoss/grimoirelab-perceval-opnfv/actions?query=workflow:tests+branch:master+event:push) [![Coverage Status](https://img.shields.io/coveralls/chaoss/grimoirelab-perceval-opnfv.svg)](https://coveralls.io/r/chaoss/grimoirelab-perceval-opnfv?branch=master)

Bundle of Perceval backends for OPNFV ecosystem.

## Backends

The backends currently managed by this package support the next repositories:

* Functest

## Requirements

These set of backends requires Python 3.7 or later, and
[Perceval](https://github.com/chaoss/grimoirelab-perceval/) to run.
For other Python dependencies, please check the `pyproject.toml`
file included on this repository.

## Installation

To install this package you will need to clone the repository first:

```
$ git clone https://github.com/grimoirelab/perceval-opnfv.git
```

Then you can execute the following commands:
```
$ pip3 install -r requirements.txt
$ pip3 install -e .
```

In case you are a developer, you should execute the following commands to install Perceval in your working directory (option `-e`) and the packages of requirements_tests.txt.
```
$ pip3 install -r requirements.txt
$ pip3 install -r requirements_test.txt
$ pip3 install -e .
```

## Examples

### Functest

```
$ perceval functest http://testresults.opnfv.org/test/ --from-date 2017-06-01 --to-date 2017-06-02
```

## License

Licensed under GNU General Public License (GPL), version 3 or later.
