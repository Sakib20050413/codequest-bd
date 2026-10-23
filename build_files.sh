#!/usr/bin/env bash
set -o errexit
python3 -m pip install -r requirements.txt --break-system-packages || python3 -m pip install -r requirements.txt
python3 manage.py collectstatic --noinput --clear
python3 manage.py migrate --noinput
python3 manage.py seed_lessons || python3 seed_codequest.py
