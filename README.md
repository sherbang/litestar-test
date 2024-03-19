# Boilerplate for New Projects

## Overview
This is a basic example Python program with testing and code quality tooling.

The example program is an implementation of [FizzBuzz](https://blog.codinghorror.com/why-cant-programmers-program/):
Write a program that prints the numbers from 1 to 100. But for multiples of three print “Fizz” instead of the number
and for the multiples of five print “Buzz”. For numbers which are multiples of both three and five print “FizzBuzz”.

## Dev Prerequisites
- python 3.12
  - Recommend installing with pyenv
  - Recommend installing pipx as well to manage our other tools
- pre-commit
    ```shell
    pipx install pre-commit
    ```
- poetry
    ```shell
    pipx install poetry
    ```
- Optional: Linters
    ```shell
    pipx install ruff
    pipx install pyright
    ```

## Linux Dev Installation

```bash
# Initialize poetry
which python3.12 | xargs poetry env use
poetry install --with=dev

# Install git pre-commit hooks
pre-commit install
```

## Usage

### Running the app
```bash
poetry run ./pysrc/fizzbuzz
```

### Running tests
```bash
poetry run pytest
```

### Running linters
```bash
pre-commit run -a
pyright pysrc
```
