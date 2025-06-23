#!/bin/bash
pip install -r requirements.txt
python manage.py migrate
python manage.py collectstatic --noinput  # Only for static files