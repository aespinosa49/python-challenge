import os
import csv

month_total = 0
total_profit = 0
total_profit_change = 0
max_profit = 0
min_profit = 0
max_month = 0
min_month = 0

budget_data = os.path.join("Resources", "budget_data.csv")
with open(budget_data) as csvFile:
    csvReader = csv.reader(csvFile, delimiter =',')
    next(csvReader, None)

    for row in csvReader:
        month_total = month_total + 1
        total_profit = total_profit + 2


       
print(f"Financial Analysis:")
print("-------------------------------------------------------")
print(f"Total Months: {month_total}")
print(f"Total Revenue: {total_profit} USD")
print(f"Average Revenue Change: {total_profit_change} USD")
print(f"Greatest Increase in Profits: {max_month} {max_profit} USD")
print(f"Greatest Decrease in Profits: {min_month} {min_profit} USD")
print("")