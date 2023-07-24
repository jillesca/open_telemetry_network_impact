# syntax=docker/dockerfile:1
FROM python:alpine3.16 AS base
COPY ./docker/requirements.txt .
RUN apk add \
    gcc \
    musl-dev \
    linux-headers \
    libssh-dev \
    openssh-client \
    && pip install --upgrade pip \
    && pip3 install -r requirements.txt
WORKDIR /home



FROM base as cml

ARG CML_LAB
ARG CML_HOST
ARG CML_USERNAME
ARG CML_PASSWORD
ARG CML_VERIFY_CERT

ENV CML_LAB=${CML_LAB}
ENV CML_HOST=${CML_HOST}
ENV CML_USERNAME=${CML_USERNAME}
ENV CML_PASSWORD=${CML_PASSWORD}
ENV CML_VERIFY_CERT=${CML_VERIFY_CERT}

RUN pip install virl2-client==2.5.0 \
    && ansible-galaxy collection install cisco.cml

