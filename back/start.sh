#!/bin/bash
sleep 5
python mysite/manage.py makemigrations
python mysite/manage.py migrate
python mysite/manage.py collectstatic --noinput
uwsgi --socket :8001 --module mysite.wsgi --chdir mysite --buffer-size=32768

