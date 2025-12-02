#!/usr/bin/env bash
echo "Starting build..."

pip install -r requirements.txt

python photo_contest/manage.py migrate --noinput
python photo_contest/manage.py collectstatic --noinput --clear

echo "Build complete!"
