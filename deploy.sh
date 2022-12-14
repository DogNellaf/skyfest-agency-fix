#!/bin/bash
git pull
source venv/bin/activate
find . -type f -name "*.pyc" -exec rm -f {} \;
pip install -r requirements.txt
yes "yes" | python manage.py migrate
python manage.py collectstatic --noinput
chown www-data:www-data -R .
touch venv/uwsgi.reload
