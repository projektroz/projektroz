FROM python:3.11-slim

RUN pip install --upgrade pip 

RUN apt-get update && apt-get install -y --no-install-recommends \
    postgresql-server-dev-all \
    gcc \
    libc-dev \
    libpq5 \
    xvfb
COPY ./requirements.txt .
RUN pip install psycopg2
RUN pip install -r requirements.txt

COPY . /app
WORKDIR /app

COPY ./entrypoint.sh .
ENTRYPOINT ["sh", "/app/entrypoint.sh"]
