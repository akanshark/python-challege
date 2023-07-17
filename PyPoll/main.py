import os
import csv
totalvotes = 0
candidates = []
candidate_vote = []
csvpath = os.path.join("..", "Resources", "election_data.csv")
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimeter = ',')
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    for row in csvreader:
        totalvotes +=1
        if row(3) not in candidates:
            candidates.append(row(3))
            candidate_vote.append(1)
        else:
            index = candidates.index(row(3))
            candidate_vote[index]+=1
for candidate in candidates:
    index = 0
    print(candidate + ": " + (candidate_vote[index]/totalvotes)*100 +"% (" + candidate_vote[index] + ")")
winner_index = candidate_vote.index(max(candidate_vote))
print("Winner: " + candidate[winner_index])