#!/bin/sh
while ! curl -s http://localhost:8000 > /dev/null; do
    sleep 1
done
sleep 5 
python manage.py makemigrations --noinput
python manage.py migrate --noinput
