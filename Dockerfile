FROM --platform=linux/amd64 python:3.12-slim-bullseye
RUN pip3 install poetry
RUN apt-get update

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONIOENCODING=utf-8 \
    POETRY_NO_INTERACTION=1 \
    POETRY_CACHE_DIR=/tmp/poetry_cache \
    PYTHONPATH="/app:$PYTHONPATH"

WORKDIR /app

COPY pyproject.toml poetry.lock ./
RUN pip3 install --upgrade pip
RUN poetry config virtualenvs.create false

RUN poetry install --without dev --no-root && rm -rf $POETRY_CACHE_DIR

COPY src ./src
COPY .env /app/src/.env

WORKDIR /app/src

EXPOSE 80

CMD ["python", "main.py"]
