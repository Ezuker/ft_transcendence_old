FROM python:3.11-slim-buster

WORKDIR /usr/src/app

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN pip install --upgrade pip pipenv flake8
COPY Pipfile* ./
RUN pipenv install --deploy --ignore-pipfile

COPY . .

# RUN flake8 --ignore=E501,F401 .