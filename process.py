import boto3
import csv
import os

INPUT_BUCKET = "banking-batch-input-hardik"
OUTPUT_BUCKET = "banking-batch-output-hardik"
INPUT_FILE = "transactions_2026_01_02.csv"
OUTPUT_FILE = "report_2026_01_02.txt"

s3 = boto3.client("s3")

print("Downloading file from S3...")
s3.download_file(INPUT_BUCKET, INPUT_FILE, INPUT_FILE)

balances = {}

with open(INPUT_FILE) as f:
    reader = csv.DictReader(f)
    for row in reader:
        acc = row["account_id"]
        amt = float(row["amount"])
        if row["type"] == "DEBIT":
            balances[acc] = balances.get(acc, 0) - amt
        else:
            balances[acc] = balances.get(acc, 0) + amt

with open(OUTPUT_FILE, "w") as f:
    for acc, bal in balances.items():
        f.write(f"{acc},{bal}\n")

print("Uploading report to S3...")
s3.upload_file(OUTPUT_FILE, OUTPUT_BUCKET, OUTPUT_FILE)

print("Batch job completed successfully.")

