# Gemini Project Configuration

## Project Overview

This project is a web application with a Django backend and a TypeScript-based frontend.

## Key Technologies

- **Backend:** Django
- **Database:** PostgreSQL
- **Frontend:** TypeScript (specific framework to be determined)
- **Dependency Management:** `uv`
- **Linting:** `ruff`
- **Local Development:** Docker Compose

## Development Focus

- **Testing:** A strong emphasis is placed on comprehensive testing. All new features should be accompanied by tests.
- **Code Formatting:** Code should be well-formatted and adhere to consistent style guidelines using `ruff`.
- **CI/CD:** The project utilizes GitHub Actions to automate checks (linting and testing) and deployment.

## Useful Commands

- **Run local development server:** `docker compose up`
- **Run tests locally:** `./run_tests.sh`
- **Run linter and fix issues:** `./run_lint.sh`
- **Create a superuser:** `docker compose exec web uv run python manage.py createsuperuser`