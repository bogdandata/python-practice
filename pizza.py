import sys
from tabulate import tabulate
import csv

table = []

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
if sys.argv[1].endswith(".csv") == False:
    sys.exit("Not a CSV file")
try:
    with open(sys.argv[1]) as file:
        reader = csv.reader(file)
        for row in reader:
            table.append(row)
except FileNotFoundError:
    sys.exit("File does not exist")

print(tabulate(table, headers="firstrow", tablefmt="grid"))
    