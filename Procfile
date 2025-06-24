release: python manage.py collectstatic --noinput
web: python manage.py migrate && gunicorn socialmedia.wsgi --workers 2 --timeout 120 --bind 0.0.0.0:$PORT