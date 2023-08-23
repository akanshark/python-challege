import os
import csv

NAME_INDEX = 2
CSV_PATH = os.path.join("Resources", "election_data.csv")
OUTPUT_PATH = os.path.join("Analysis", "election_results.txt")

totalvotes = 0
candidates = []
candidate_votes = {}
winning_votes = 0
percentages = {}


os.chdir(os.path.dirname(os.path.realpath(__file__))) # use in vscode
with open(CSV_PATH) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    for row in csvreader:
        name = row[NAME_INDEX]
        totalvotes +=1
        if name not in candidate_votes:
            candidate_votes[name] = 1 
            candidates.append(name)    # here to fulfill assignment req
        else:
            candidate_votes[name] += 1

for name in candidate_votes:
    votes = candidate_votes[name]
    if votes > winning_votes:
        winning_votes = votes
        winning_name = name
    percentages[name] = round(100*votes/totalvotes, 3)

results_str = ''
for candidate in candidate_votes:
    results_str += f"{candidate}: {candidate_votes[candidate]}, {percentages[candidate]}%\n"


full_results = (
    "Elections\n" 
    "---------\n"
    f"Total Votes: {totalvotes}\n"
    "---------\n"
    f"{results_str}\n"
    "---------\n"
    f"Winner: {winning_name}\n"
    "---------\n"
)

with open(OUTPUT_PATH, "w") as output_file:
    output_file.write(full_results)
print(full_results)