FROM python:3.8.10-slim-buster

RUN apt-get update && \
    apt-get install -y --no-install-recommends

LABEL maintainer = "f-teruhisa <teru_fukumoto@outlook.jp>"

ENV LANG ja_JP.UTF-8
ENV LANGUAGE ja_JP:ja
ENV LC_ALL ja_JP.UTF-8
ENV TZ JST-9

RUN mkdir /app
COPY . /app
WORKDIR /app

RUN pip install --upgrade pip && \
    pip install --upgrade setuptools && \
    pip install --no-cache-dir -r requirements.txt

CMD ["python", "main.py"]