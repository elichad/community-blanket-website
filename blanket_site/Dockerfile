# syntax=docker/dockerfile:1
# for Django webserver
FROM python:3.12-slim
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code

# install dependencies
COPY . /code/
RUN pip install -r requirements.txt
