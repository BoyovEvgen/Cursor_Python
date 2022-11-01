# Python classes practice

## Homework
- Create function that visualize header
```
@classmethod
def show_header(cls):
    ...
```
_example_
```
-------------------------------------------------------------------------
| Name                           | Balance    | Taxes Pay  | Salary     |
-------------------------------------------------------------------------
```
- Create function that show all employees
```
@timer
def show_table():
    ...
```
_example_
```
-------------------------------------------------------------------------
| John works 165 day(s).         | 1815       | 1650       | 165        |
-------------------------------------------------------------------------
| Alex works 184 day(s).         | 9200       | 3680       | 5520       |
-------------------------------------------------------------------------
| Kseniya works 175 day(s).      | 8750       | 7000       | 1750       |
-------------------------------------------------------------------------
| Valeriy works 195 day(s).      | 11700      | 9750       | 1950       |
-------------------------------------------------------------------------
| Vera works 1261 day(s).        | 124839     | 75660      | 49179      |
-------------------------------------------------------------------------
| Suzanna works 530 day(s).      | 10600      | 5300       | 5300       |
-------------------------------------------------------------------------
| Gleb works 530 day(s).         | 10600      | 5300       | 5300       |
-------------------------------------------------------------------------
```
- Update rate for all employees and visualize new table
- ADDITIONAL: Update timer decorator so that it displays a message with the name of the function (We must pass the name as an argument)

_example_
```
@timer(func_name = "Show table ")
def show_table():
    ...
```
```
def timer(func_name: str = "Function "):
    ...
```

## Requirements:

- black
- flake8
- [make](https://en.wikipedia.org/wiki/Make_(software)) is recommended

_WARNING: makefile commands may be different depends on OS (here should work from linux and mac os)_

## Setup

_Please try to use Make commands_

**Create virtual environment**
```
$ make
```
**Setup virtual environment**

- upgrade PIP
- install wheel and setuptools
- install requirements from requirements.txt

```
$ make setup
```
**Check code quality**

- black
- flake8

_For flake8 we need tox.ini file with configs_

```
$ make lint
```
**Run main.py**
```
$ make run
```
