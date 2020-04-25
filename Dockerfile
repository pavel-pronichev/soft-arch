FROM python:3-slim

RUN apt-get update && apt-get upgrade \
    && pip install --upgrade pip

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.* \
    && pip freeze

WORKDIR app

COPY run.sh .
COPY src/ .

RUN ls -al

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]


