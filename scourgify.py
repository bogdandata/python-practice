import sys
import csv

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
if not sys.argv[1].endswith(".csv") or not sys.argv[2].endswith(".csv"):
    sys.exit("Not a CSV file")
try:
    with open(sys.argv[1]) as file, open(sys.argv[2], "w") as file2:
        reader = csv.DictReader(file)
        writer = csv.DictWriter(file2, fieldnames=["first", "last", "house"])
        writer.writeheader()
        for row in reader:
            last, first = row["name"].split(", ")
            writer.writerow({"first": first, "last": last, "house": row["house"]})
except FileNotFoundError:
    sys.exit(f"could not read file {sys.argv[1]}")
        