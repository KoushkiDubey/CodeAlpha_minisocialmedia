#!/bin/bash
# Exit immediately if any command fails
set -e

echo "---- Installing dependencies ----"
pip install -r requirements.txt

# Only attempt DB operations if DATABASE_URL exists
if [ -n "${DATABASE_URL}" ]; then
  echo "---- Running migrations ----"
  python manage.py migrate --noinput

  echo "---- Collecting static files ----"
  python manage.py collectstatic --noinput
else
  echo "WARNING: DATABASE_URL not set, skipping database operations"
fi--noinput  # Only for static files