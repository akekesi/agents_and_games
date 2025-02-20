# Agents and Games

## Table of Contents
1. [Description](#description)
1. [Demo](#demo)
1. [Prerequisites](#prerequisites)
1. [Python Environment Setup](#python-environment-setup)
1. [Authors](#authors)
1. [Acknowledgements](#acknowledgements)
1. [License](#license)

## Description
🚧 This project is a work in progress. Some features may be incomplete, untested, or lacking full documentation. 🚧  

## Installing Python Packages
```bash
$ python -m pip install --upgrade pip
$ pip install -r requirements.txt
$ pip install -r requirements_dev.txt
```

## Running `main.py`
```bash
$ python -m src.main
```

## Running Pylint (with `requirements_dev.txt`)
```bash
$ pylint src/<name_of_file>
```

## Running a Single Unit Test (with `requirements_dev.txt`)
```bash
$ python -m tests.<name_of_test_file>
```

## Running All Unit Tests (with `requirements_dev.txt`)
```bash
$ python -m unittest discover tests
```

## Running Coverage with Unit Tests (with `requirements_dev.txt`)
```bash
$ coverage run -m unittest discover tests
$ coverage report
$ coverage html
```
View the HTML coverage report at: `htmlcov/index.html`

## Authors
Attila Kékesi

## Acknowledgements
- [Tic-Tac-Toe](https://de.wikipedia.org/wiki/Tic-Tac-Toe)
- [Connect4](https://en.wikipedia.org/wiki/Connect_Four)

## License
Code released under the [MIT License](https://github.com/akekesi/connect4/blob/main/LICENSE).
