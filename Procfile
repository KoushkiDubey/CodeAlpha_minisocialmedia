release: python manage.py migrate --noinput && python manage.py collectstatic --noinput
web: gunicorn socialmedia.wsgi --workers 2 --timeout 120 --bind 0.0.0.0:$PORT