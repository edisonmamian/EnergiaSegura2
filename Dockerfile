FROM python:3.9-alpine3.14
WORKDIR /code
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
COPY ./requeriments.txt .
RUN pip install --upgrade pip && \
    pip install -r requeriments.txt