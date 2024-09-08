# Dockerfile for service-b
FROM python:3.9-slim

WORKDIR /app

COPY service-b.py /app
COPY ../requirements.txt /app

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "service-b.py"]
