FROM python:3.7.3-stretch
MAINTAINER Asadov Ahmed zoxon470@gmail.com

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY Pipfile Pipfile.lock ./
RUN pip install pipenv
RUN pipenv install --system

COPY . .

ENTRYPOINT ["python", "./main.py"]
