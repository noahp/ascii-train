FROM python:3.7-alpine

COPY . /app
WORKDIR /app

RUN python setup.py test

RUN python setup.py bdist_wheel

RUN pip install .

RUN ascii-train "hey yo"
