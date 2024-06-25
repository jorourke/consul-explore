# syntax=docker/dockerfile:1.4
FROM  python:3.12-alpine

WORKDIR /app

COPY requirements.txt /app
RUN --mount=type=cache,target=/root/.cache/pip \
    pip3 install -r requirements.txt

COPY . /app

ENTRYPOINT ["python3"]
CMD [ "./a/app.py" ]
