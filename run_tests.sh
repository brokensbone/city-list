#!/bin/bash
docker compose exec web uv run python manage.py test
