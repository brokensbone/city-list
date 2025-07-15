# Gemini Project Configuration

## Project Overview

This project is a website which tracks restaurants, bars, and food/drink shops in a city (starting with Leeds). It has two main functions:
1.  Showing the range of things available.
2.  Acting as an archive of much-missed closed places.

The backend is Django, the frontend is TypeScript-based.

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