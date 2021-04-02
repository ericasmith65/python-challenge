#Import dependencies
import os
import csv

#Create variables
votes = 0
x = 0
index = []
candidates = []
candidates_votes = []
percent_votes = []
candidates_vote_count = {}
winner = "candidate name"
#Read csv file skip header
csvpath = r'C:\Users\esmit\OneDrive\Documents\GitHub\python-challenge\PyPoll\Resources\Assignments_03-Python_PyPoll_Resources_election_data.csv'
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

#Create loop to read through file
    for row in csvreader:
        votes = votes + 1
#A complete list of candidates who received votes
        if row[2] not in candidates:
            candidates.append(row[2])
            index.append(x)
            x = x + 1
        candidates_votes.append(row[2])

print("Election Results")
print("--------------------------------------")

#The total number of votes cast
print(f"Total Votes: {votes}")
print("--------------------------------------")

#The total number of votes each candidate won
candidates_vote_count = {i:candidates_votes.count(i) for i in candidates}

#The percentage of votes each candidate won
percent_votes = [round(100*(candidates_vote_count[candidates[i]]/votes), 2) for i in index]
for i in index:
    print(f"{candidates[i]}: {percent_votes[i]}% ({candidates_vote_count[candidates[i]]})")
print("--------------------------------------")
#The winner of the election based on popular vote
max_percent = max(percent_votes)
maxlocation = percent_votes.index(max_percent)
print(f"Winner: {candidates[maxlocation]}")
#In addition, your final script should both print the analysis to the terminal and export a text file with the results
txtpath = r'C:\Users\esmit\OneDrive\Documents\GitHub\python-challenge\PyPoll\Analysis\analysis.txt'
with open(txtpath, "w") as f:
    f.write(f"Election Results\n")
    f.write(f"--------------------------------------\n")
    f.write(f"Total Votes: {votes}\n")
    f.write(f"--------------------------------------\n")
    for i in index:
        f.write(f"{candidates[i]}: {percent_votes[i]}% ({candidates_vote_count[candidates[i]]})\n")
    f.write(f"--------------------------------------\n")
    f.write(f"Winner: {candidates[maxlocation]}\n")