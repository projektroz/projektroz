FROM python:3.11.4-slim-buster

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
COPY ./backendRequirements.txt .
RUN pip install --no-cache-dir -r backendRequirements.txt

COPY . .

ENV DJANGO_SETTINGS_MODULE=projektroz.settings

RUN python manage.py migrate
RUN python manage.py collectstatic --noinput

EXPOSE 8000

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "projektroz.wsgi:application"]