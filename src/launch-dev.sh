#!/bin/bash

echo "Dev Server Launch"
echo $PWD
ls -al
which python
uv run python manage.py migrate
exec uv run python manage.py runserver 0.0.0.0:8000
