#!/usr/bin/env bash
echo "Starting build process..."

# Install requirements
pip install -r requirements.txt

# Collect static files
python manage.py collectstatic --noinput --clear

echo "Build completed successfully!"
