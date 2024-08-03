# Schedule to Google Calendar CLI

This CLI tool allows you to add events to your Google Calendar from a schedule written in a text file. It provides an easy way to bulk add events to your calendar without manually entering them through the Google Calendar interface.

## Features

- Parse a schedule from a text file
- Interact with Google Calendar API
- Add events to your Google Calendar
- [List any other key features]

## Installation

To set up this project, follow these steps:

1. Clone the repository:
   ```
   git clone https://github.com/alexander-xerxes-grant/gcal-tool.git
   cd gcal-tool
   ```

2. Set up the virtual environment using uv:
   ```
   just setup
   ```

3. Activate the virtual environment:
   ```
   source .venv/bin/activate  # On Unix-based systems
   # or
   .venv\Scripts\activate  # On Windows
   ```

## Usage

[Provide basic usage instructions here. For example:]

1. Prepare your schedule in a text file (e.g., `schedule.txt`) in the required format.

2. Run the CLI tool:
   ```
   schedule-to-gcal add schedule.txt
   ```

3. Follow the prompts to authenticate with your Google account (first time only).

4. The events will be added to your Google Calendar.

## Configuration

[Add config steps such as setting up Google Calendar API]

## Development

This project uses modern Python tooling for development:

- `just`: Command runner for common tasks
- `uv`: For managing virtual environments
- `black`: For code formatting
- `isort`: For import sorting
- `ruff`: For linting
- `pytest`: For running tests

To run development tasks:

- Format code: `just format`
- Lint code: `just lint`
- Run tests: `just test`
- Run all checks: `just check`
