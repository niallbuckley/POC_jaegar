# Dockerfile for service-b
FROM python:3.9-slim

WORKDIR /app

COPY service-b/service-b.py /app
COPY requirements.txt /app

RUN apt-get -qq update \
    && apt-get install -y --no-install-recommends g++ \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "service-b.py"]
