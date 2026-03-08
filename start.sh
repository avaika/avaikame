#!/bin/bash
set -e

cd /app/avaika.me

python manage.py migrate --noinput
python manage.py collectstatic --noinput
gunicorn project.wsgi:application --bind 0.0.0.0:8000 --workers 3
