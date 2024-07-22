# Variables
PYTHON_VERSION = 3.12
POETRY_VERSION = 1.8.3
VENV_DIR = .venv

# Default target
.PHONY: all
all: setup install run

check_python:
	@echo "Checking for Python $(PYTHON_VERSION)..."
	@python --version | grep -E "Python $(PYTHON_VERSION)" > /dev/null || (echo "Python $(PYTHON_VERSION) is not installed." && exit 1)

# Create virtual environment
.PHONY: setup
setup: check_python
	@echo "Setting up virtual environment..."
	python -m venv $(VENV_DIR)
	@echo "Virtual environment created in $(VENV_DIR)"

# Install dependencies
.PHONY: install
install: setup
	@echo "Setting up python requirements..."
	$(VENV_DIR)/bin/pip install --upgrade pip
	$(VENV_DIR)/bin/pip install poetry==$(POETRY_VERSION)
	$(VENV_DIR)/bin/poetry install

# Run the application
.PHONY: run
run:
	$(VENV_DIR)/bin/poetry run start

# Run tests
.PHONY: test
test:
	@echo "Running tests..."
	$(VENV_DIR)/bin/poetry run pytest

# Lint the code
.PHONY: lint
lint:
	@echo "Running linter to check only..."
	$(VENV_DIR)/bin/ruff check .

# Lint and fix the code
.PHONY: lint-fix
lint-fix:
	@echo "running linter and fixing where possible..."
	$(VENV_DIR)/bin/ruff check . --fix

.PHONY: type
type:
	@echo "Checking types with mypy..."
	$(VENV_DIR)/bin/mypy .

# Run status checks
.PHONY: status
status: lint test type

# Format the code
.PHONY: format
format:
	@echo "Formating code using ruff..."
	$(VENV_DIR)/bin/ruff format .

.PHONY: tidy
tidy: format lint-fix

.PHONY: package
package:
	$(VENV_DIR)/bin/pyside6-deploy epii/main.py

.PHONY: clean
clean:
	@echo "Removing generated files..."
	find . -type f -name "*.pyc" -delete
	find . -type f -name "main.bin" -delete
	find . -type f -name "pysidedeploy.spec" -delete
	find . -type d -name "__pycache__" -exec rm -r {} +
	find . -type d -name ".ruff_cache" -exec rm -r {} +
	find . -type d -name ".pytest_cache" -exec rm -r {} +

.PHONY: remove
remove: clean
	@echo "Removing virtual environment..."
	rm -rf $(VENV_DIR)