FROM python:3.9-slim

WORKDIR /app

COPY process.py .
COPY transactions.csv .

CMD ["python", "process.py"]
