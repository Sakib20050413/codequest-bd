#!/usr/bin/env bash
python3 -m pip install -r requirements.txt --break-system-packages || python3 -m pip install -r requirements.txt
python3 manage.py makemigrations learn --noinput || true
python3 manage.py migrate --noinput
python3 seed_codequest.py
python3 manage.py collectstatic --noinput --clear
