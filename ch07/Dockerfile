FROM python:3.10-alpine AS builder

EXPOSE 8000

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN apk update
RUN apk add --no-cache gcc musl-dev mariadb-connector-c-dev mariadb-dev
RUN pip install --no-cache-dir -r requirements.txt
