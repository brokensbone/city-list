# City List Project

A web application with a Django backend.

## Overview

This project is a website which tracks restaurants, bars, and food/drink shops in a city, starting with Leeds. It has two main functions:

1.  Showcasing the range of currently open and available places.
2.  Acting as an archive of much-missed closed places.

The backend is built with Django and uses a PostgreSQL database. The development environment is containerized using Docker Compose for consistency and ease of use.

The project is set up with a focus on code quality, with automated linting and testing pipelines.

## Data Models

The core data is organized into two main models within the `places` app:

-   **`BusinessGroup`**: Represents a parent company or group that may own multiple individual businesses (e.g., a coffee shop chain).
-   **`Business`**: Represents a single establishment. It includes details like its name, category (Restaurant, Bar, Shop), location (latitude/longitude), and its opening and closing dates. Each `Business` must belong to a `BusinessGroup`.

These models are accessible and manageable via the Django admin interface.

## Getting Started

### Prerequisites

- Docker and Docker Compose
- `uv` (for local Python environment management if not using Docker for everything)

### Setup

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd city-list
    ```

2.  **Start the development environment:**
    This command will build the Docker images and start the Django development server and the PostgreSQL database.
    ```bash
    docker compose up --build
    ```
    The application will be available at [http://localhost:8000](http://localhost:8000).

## Local Development

A few scripts are provided to streamline common development tasks.

- **Run Tests:**
  To execute the test suite against the running container:
  ```bash
  ./run_tests.sh
  ```

- **Run Linter:**
  To check for linting issues with `ruff` and apply automatic fixes:
  ```bash
  ./run_lint.sh
  ```

- **Create a Superuser:**
  To create an admin user for accessing the Django admin interface:
  ```bash
  docker compose exec web uv run python manage.py createsuperuser
  ```

## CI/CD

This project uses GitHub Actions for continuous integration. On every pull request to the `main` branch, the following checks are performed:
- **Linting:** Code is checked for style and formatting issues using `ruff`.
- **Testing:** The full Django test suite is run against a PostgreSQL database.