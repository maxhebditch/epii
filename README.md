# Project Name

## Description
epii is a new approach

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

### MVVMC Architecture

- Model
    - Pure abstraction layer to represent the data
    - Handles all aspects of reading, writing and validating notes
- ViewModel
    - Sits between the View and the Model updating both as required
    - Takes the Model as a reference and makes changes to it when required by the View
    - When changes are made it emits signals which are listened to by the View
- View
    - The View consists solely of UI elements for user interaction
    - It presents data from the ViewModel to the user
    - It captures user input and uses this to change the presented data via the ViewModel


## License

This project is licensed under the [MIT License](./LICENSE).
