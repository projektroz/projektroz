FROM python:3.11-alpine

RUN pip install --upgrade pip 

RUN apk update && apk add postgresql-dev gcc libc-dev libpq xvfb

COPY ./requirements.txt .

RUN pip install -r requirements.txt

COPY . /app
WORKDIR /app
RUN apk add curl
COPY ./entrypoint.sh .
ENTRYPOINT ["sh", "/app/entrypoint.sh"]
