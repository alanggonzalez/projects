FROM python:3.11-slim

WORKDIR /app

RUN set -xe \
    && apt-get update \
    && apt-get install python3-pip -y \
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "app.py"]
