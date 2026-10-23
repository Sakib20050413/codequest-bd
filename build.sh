#!/usr/bin/env bash
# Exit on error
set -o errexit

python -m pip install --upgrade pip
pip install -r requirements.txt

python manage.py collectstatic --no-input --clear
python manage.py migrate --no-input
python manage.py seed_lessons
