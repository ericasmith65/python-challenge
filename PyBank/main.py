import os
import csv

csvpath = os.path.join('..', 'Resources', 'Assignments_03-Python_PyBank_Resources_budget_data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    For row in csvreader
        