FROM python:3.9-slim

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY poetry.lock pyproject.toml ./

RUN pip install poetry \
  && apt-get update \
  && poetry config virtualenvs.create false \
  && poetry install