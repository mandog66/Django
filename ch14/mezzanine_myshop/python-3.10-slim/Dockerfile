FROM python:3.10-slim AS builder

EXPOSE 8000

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN apt-get update && apt-get -y install locales-all
RUN pip install --no-cache-dir -r requirements.txt -U
