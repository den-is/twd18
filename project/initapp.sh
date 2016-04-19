#!/bin/bash

# Make app container wait until postgres container accepts connections at 5432 port.
# Otherwise run migrate manually
python manage.py migrate

# Collect static files in static_root which will be served by nginx
#python manage.py collectstatic -v0 --noinput

# Don't forget to create super user, manualy
# python manage.py createsuperuser

# Development server
# python manage.py runserver 0.0.0.0:8000

# Single line gunicorn command
# gunicorn config.wsgi:application -n rango_app -b 0.0.0.0:8000 -w 3 -t 300 --log-level debug --log-file ./logs/error.log --access-logfile ./logs/access.log --reload

gunicorn config.wsgi:application \
  --name rango_app \
  --bind 0.0.0.0:8000 \
  --workers 3 \
  --log-level debug \
#  --log-file ./logs/error.log \
#  --access-logfile ./logs/access.log \
  --reload
#  --timeout 300 \
