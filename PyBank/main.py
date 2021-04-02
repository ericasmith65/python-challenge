import os
import csv
import math

csvpath = r"C:\Users\esmit\OneDrive\Documents\GitHub\python-challenge\PyBank\Resources\Assignments_03-Python_PyBank_Resources_budget_data.csv"
#The total number of months included in the dataset
month_count = 0
#The net total amount of "Profit/Losses" over the entire period
profit_losses_total = 0

#Calculate the changes in "Profit/Losses" over the entire period
changes = []
change = 0
profit_loss = 0
date = []



with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    for row in csvreader:
        month_count = int(month_count) + 1
        profit_losses_total = int(profit_losses_total) + int(row[1]) 
        change = int(row[1]) - int(profit_loss)
        changes.append(change)
        profit_loss = int(row[1])
        date.append(row[0])
changes.pop(0)
date.pop(0)

print(f"The number of months was {month_count}")
print(f"The total amount of profits/losses equaled ${profit_losses_total}")
#The greatest decrease in profits (date and amount) over the entire period
minimum = min(changes)
milocation = changes.index(minimum)
print(f"The greatest decrease in losses equaled ${minimum}, and occured in {date[milocation]}")
#The greatest increase in losses (date and amount) over the entire period
maximum = max(changes)
malocation = changes.index(maximum)
print(f"The greatest increase in profits equaled ${maximum}, and occured in {date[malocation]}")
#Find the average of those changes
average = round(sum(changes)/(month_count - 1), 2)
print(f"The average of profits/losses changes equaled ${average}")

txtpath = r'C:\Users\esmit\OneDrive\Documents\GitHub\python-challenge\PyBank\Analysis\analysis.txt'
with open(txtpath, "w") as f:
    f.write(f"The number of months was {month_count}\n")
    f.write(f"The total amount of profits/losses equaled ${profit_losses_total}\n")
    f.write(f"The greatest decrease in losses equaled ${minimum}, and occured in {date[milocation]}\n")
    f.write(f"The greatest increase in profits equaled ${maximum}, and occured in {date[malocation]}\n")
    f.write(f"The average of profits/losses changes equaled ${average}\n")
