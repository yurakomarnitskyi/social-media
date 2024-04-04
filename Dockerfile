FROM python:latest

WORKDIR /root/my_app/

COPY ./requirements.txt .

RUN pip install -r requirements.txt

COPY ./apps ./apps
