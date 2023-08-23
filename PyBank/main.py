import os
import csv

NAME_INDEX = 2
CSV_PATH = os.path.join("Resources", "budget_data.csv")
OUTPUT_PATH = os.path.join("Analysis", "budget_results.txt")

os.chdir(os.path.dirname(os.path.realpath(__file__))) # use in vscode

monthcount = 0
net_total = 0
avg_change = 0
prev_month = 0
inc = 0
dec = 0
incm = ""
decm = ""

with open(CSV_PATH) as csvfile:
    csvreader = csv.reader(csvfile, delimiter  = ',')
    print(csvreader)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    for row in csvreader:
        monthcount+=1
        net_total = net_total + int(row[1])
        change = int(row[1]) - prev_month
        avg_change += change
        if change > inc:
            inc = change
            incm = str(row[0])
        if change < dec:
            dec = change
            decm = str(row[0])
        prev_month = int(row[1])

avg_change = avg_change/monthcount # error?

full_results = (
    f"Total Months: {monthcount}\n"
    f"Total: ${net_total}\n"
    f"Average Change: ${avg_change}\n"
    f"Greatest Increase in Profits: ${incm} ({inc})\n"
    f"Greatest Decrease in Profits: ${decm} ({dec})\n"
)

with open(OUTPUT_PATH, "w") as output_file:
    output_file.write(full_results)
print(full_results)