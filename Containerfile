FROM python:latest

COPY . /package/

WORKDIR /package

RUN python -m pip install --upgrade --no-cache-dir pip pytest \
    && python -m pip install --no-cache-dir .

RUN python -m pytest -vvs

