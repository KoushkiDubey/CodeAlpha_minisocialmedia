#!/bin/bash
if [ -z "${DATABASE_URL}" ]; then
  echo "ERROR: DATABASE_URL not set!" >&2
  exit 1
fi
pip install -r requirements.txt
python manage.py migrate
python manage.py collectstatic --noinput  # Only for static files