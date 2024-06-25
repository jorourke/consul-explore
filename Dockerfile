# syntax=docker/dockerfile:1.4
FROM  python:3.12-alpine

WORKDIR /app

COPY src/requirements.txt /app
RUN --mount=type=cache,target=/root/.cache/pip \
    pip3 install -r requirements.txt

COPY ./src /app/src

CMD [ "/bin/sh" ]
