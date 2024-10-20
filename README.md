# Project Name

## Description

epii is a new approach to understanding notes as a stream.

## Installation

1. Clone the repository.
2. Ensure you have python 3.12 active
3. Install python requirements
    + Run `make install` to setup a virtual environment and install requirements automatically or install them manually from the `pyproject.toml`

## Usage

You can run the application in one of three ways.

1. `python epii/main.py`
2. `poetry run start`
3. `make run`

## Development

### MVVM Architecture

epii employs a modular MVVM structure to separate concerns using the following logic:

+ Model
  + Serves as a pure abstraction layer to represent the data
  + Handles all aspects of reading, writing, and validating notes
+ ViewModel
  + Acts as an intermediary between the View and the Model, updating both as needed
  + References the Model and modifies it when required by the View
  + Emits signals upon changes, which are then listened to by the View
+ View
  + Comprises solely of UI elements for user interaction
  + Presents data from the ViewModel to the user
  + Captures user input and utilizes it to modify the presented data via the ViewModel

### Reproducible Builds

Poetry (v1.8.3) is used for dependency management, providing a lock file and a dependency tree developed against a pinned version of Python (v3.12).
A Makefile automates the build process using a virtualenv, both locally and on GitHub Actions.

### Testing

pytest is used for unit and integration testing, along with PySide6.QtTest components for testing GUI features.
These tests, including GUI tests, run both locally and on GitHub Actions.
The CI process requires a minimum test coverage of 90% to pass, and the current test line coverage stands at 100%

### Rule based code quality checks

Ruff is used for linting, with all rules enabled except for three minor rules.
Additionally, Ruff handles code formatting.

### Type Safety and data validation

To improve code quality, reduce bugs and improve readability we use mypy and pydantic.
mypy is used for static type checking, in strict mode to ensure maximum type safety.
Pydantic is used for data validation and defining data structures.

## Continious Integration

To maintain code quality and maintain stability the CI process requires that the following criteria are met before any merges to the main branch are accepted

1. Build Verification and Reproducability: The code builds in a clean test environment
2. Testing: the code must achieve over 90% test coverage
3. Automated Code Quality Checks: pass Ruff linting with almost all the rules turned on
4. Type Safety: must satisfy mypy validation in strict mode.

## License

This project is licensed under the [MIT License](./LICENSE).
