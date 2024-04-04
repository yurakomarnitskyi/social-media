FROM python:latest

ENV PYTHONUNBUFFERED=1

WORKDIR /application 

COPY ./apps /application/

RUN pip install -r requirements





