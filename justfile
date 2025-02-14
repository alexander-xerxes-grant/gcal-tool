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
    black src tests
    isort src tests

# Lint the code
lint:
    ruff src tests

# Run tests
test:
    pytest

# Run all quality checks
check: format lint test
