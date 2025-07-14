# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y libpq-dev

# Install uv
RUN pip install uv

# Copy the dependency files and install dependencies
COPY pyproject.toml uv.lock ./
RUN uv sync

# Copy the rest of the application's code into the container
COPY . .

# Expose the port the app runs on
EXPOSE 8000

# Run the development server
CMD ["uv", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]
