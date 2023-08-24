FROM python:3.10-alpine

ARG run_env
ENV env $run_env

LABEL "Autor"="Aleksei Golubenko"
LABEL "GitHub"="https://github.com/Rafolk"

WORKDIR ./usr/tests

VOLUME ./allure-results

RUN apk update && apk upgrade && apk add bash

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY . .

CMD pytest -m "$env" tests/. --alluredir=allure-results
