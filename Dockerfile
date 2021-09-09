# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

WORKDIR /app

COPY requirements-flask.txt requirements-flask.txt

RUN pip3 install -r requirements-flask.txt

COPY websiteFunctions/flaskApp .

CMD [ "gunicorn", "--bind=0.0.0.0:5000", "--workers=2", "app:app" ]
