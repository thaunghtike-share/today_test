FROM python:3.11

WORKDIR /app

RUN pip install poetry
COPY poetry.lock /app/
COPY pyproject.toml /app/
RUN poetry export --without-hashes -f requirements.txt --output requirements.txt
RUN pip install -r requirements.txt