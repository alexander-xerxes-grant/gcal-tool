# justfile
set dotenv-load

# List available commands
default:
    @just --list

# Set up the project
setup:
    uv venv
    uv pip install -e .
    pre-commit install

# Format the code
format:
    black .
    isort .

# Lint the code
lint:
    ruff check

# Fix linted code
lint-fix:
    just format
    ruff check --fix

# Run tests
test:
    pytest

# Run all quality checks
check: format lint test
