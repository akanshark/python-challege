import os
import csv
csvpath = os.path.join("..", "Resources", "budget_data.csv")
monthcount = 0
net_total = 0
avg_change = 0
inc = 0
dec = 0
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimeter = ',')
    print(csvreader)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    for row in csvreader:
        monthcount+=1
        net_total = net_total + row[1]
        if row[1] > inc:
            inc = row[1]
        if row[1] < dec:
            dec = row[1]
avg_change = net_total/monthcount
print(monthcount + "  " + net_total + "  " + avg_change + "  " + inc + "  " + dec)

        



    

