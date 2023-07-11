import os
import csv
csvpath = os.path.join("..", "Resources", "budget_data.csv")
monthcount = 0
net_total = 0
avg_change = 0
inc = 0
dec = 0
incm = ""
decm = ""
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
            incm = row[0]
        if row[1] < dec:
            dec = row[1]
            decm = row[0]
avg_change = net_total/monthcount
print("Total Months: " + monthcount)
print("Total:  " + net_total)
print("Average Change:  " + avg_change)
print("Greatest Increase in Profits: " + incm + "(" + inc + ")")
print("Greatest Increase in Profits: " + decm + "(" + dec + ")")


with open('new.txt' 'w') as f:
    f.writelines("Total Months: " + monthcount)
    f.writelines("Total:  " + net_total)
    f.writelines("Average Change:  " + avg_change)
    f.writelines("Greatest Increase in Profits: " + incm + "(" + inc + ")")
    f.writelines("Greatest Increase in Profits: " + decm + "(" + dec + ")")

        

        



    

