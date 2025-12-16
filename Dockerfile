FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

RUN mkdir -p /app/data && chmod 777 /app/data

COPY app/ ./app
RUN pytest app/tests/

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
