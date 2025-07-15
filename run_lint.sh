#!/bin/bash
echo "Running ruff..."
uv run ruff check . --fix
echo "Running djlint..."
uv run djlint . --reformat
