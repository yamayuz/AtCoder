FROM python:3.8

WORKDIR /var/atcoder
ADD . /var/atcoder

RUN python -m pip install --upgrade pip