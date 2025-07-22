# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
	PYTHONUNBUFFERED=1 \
	UV_LINK_MODE=copy \
	UV_COMPILE_BYTECODE=1

# Set the working directory in the container
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y libpq-dev
COPY --from=ghcr.io/astral-sh/uv:0.8.0 /uv /uvx /bin/

# Copy the dependency files and install dependencies
COPY pyproject.toml uv.lock ./
RUN --mount=type=cache,target=/root/.cache/uv uv sync --locked

# Copy the rest of the application's code into the container
COPY . .

# Expose the port the app runs on
EXPOSE 8000

ENV PATH="/app/.venv/bin:$PATH"

# Run the development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
