FROM python:3.9-slim
WORKDIR /app
COPY process.py .
RUN pip install boto3
CMD ["python", "process.py"]
