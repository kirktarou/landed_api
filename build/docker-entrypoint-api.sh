#!/bin/sh

cd /api/

python manage.py migrate

python manage.py collectstatic

exec "$@"
