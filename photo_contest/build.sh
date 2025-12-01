#!/usr/bin/env bash
# build.sh for Render

echo "Starting build process..."

# Install Python dependencies
pip install -r requirements.txt

# Apply database migrations
python manage.py migrate --noinput

# Collect static files
python manage.py collectstatic --noinput --clear

echo "Build completed successfully!"