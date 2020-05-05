FROM python:3-slim

RUN apt-get update && apt-get upgrade \
    && pip install --upgrade pip

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.* \
    && pip freeze

COPY ./src/ /app

WORKDIR /app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]


