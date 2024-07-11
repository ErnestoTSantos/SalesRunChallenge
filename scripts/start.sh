#!/usr/bin/env bash
set -e

python manage.py makemigrations
python manage.py migrate

python manage.py db --create-super-user

python manage.py runserver ${DJANGO_BIND_ADDRESS}:${DJANGO_BIND_PORT}