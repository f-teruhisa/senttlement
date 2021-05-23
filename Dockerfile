FROM python:3.8.10-slim-buster
WORKDIR /app
ADD . /app

RUN pip install --upgrade pip
RUN pip install --upgrade setuptools

CMD ["python", "main.py"]