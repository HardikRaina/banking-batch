import csv

input_file = "transactions.csv"
output_file = "report.txt"

total = 0
count = 0

with open(input_file, "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        amount = float(row["amount"])
        total += amount
        count += 1

with open(output_file, "w") as f:
    f.write(f"Total transactions: {count}\n")
    f.write(f"Total amount: {total}\n")
    f.write(f"Average transaction: {total / count}\n")

print("Banking report generated successfully")
