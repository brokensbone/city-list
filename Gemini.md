# Gemini Project Configuration

## Project Overview

This project is a website which tracks restaurants, bars, and food/drink shops in a city (starting with Leeds). It has two main functions:
1.  Showing the range of things available.
2.  Acting as an archive of much-missed closed places.

The backend is Django, the frontend is TypeScript-based.

## Key Technologies

- **Backend:** Django, Django Rest Framework
- **Database:** PostgreSQL
- **API Schema:** drf-spectacular
- **Frontend:** TypeScript (specific framework to be determined)
- **Dependency Management:** `uv`
- **Linting:** `ruff` (Python), `djlint` (HTML)
- **Testing:** `factory-boy`
- **Local Development:** Docker Compose

## Data Models

- **`places` app**: Contains the core models for businesses and business groups.
- **`api` app**: Contains API views and serializers.

## API Endpoints

- **/api/status/**: Simple status check.
- **/api/businesses/**: Lists all open businesses.
- **/api/schema/**: OpenAPI schema.
- **/api/schema/swagger-ui/**: Swagger UI.

## Development Focus

- **Testing:** A strong emphasis is placed on comprehensive testing. For any new feature, I must always suggest and, upon approval, implement appropriate unit and integration tests.
- **Code Formatting:** Code should be well-formatted and adhere to consistent style guidelines.
- **CI/CD:** The project utilizes GitHub Actions to automate checks (linting and testing) and deployment.

## Useful Commands

- **Run local development server:** `docker compose up`
- **Run tests locally:** `./run_tests.sh`
- **Run linter and fix issues:** `./run_lint.sh`
- **Create a superuser:** `docker compose exec web uv run python manage.py createsuperuser`

## Final Checks

- Before completing a task, always run the local linting script to ensure code quality: `./run_lint.sh`
- Use the local Docker development environment to check that changes work: `docker compose up`
