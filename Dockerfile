FROM python:3-slim

RUN apt-get update && apt-get upgrade \
    && pip install --upgrade pip

COPY requirements.lock .

RUN pip install --no-cache-dir -r requirements.* \
    && pip freeze

WORKDIR app

COPY run.sh .
COPY src/ .

RUN ls -al

ENV ENVIRONMENT=DEV

ENTRYPOINT ["/app/run.sh"]


