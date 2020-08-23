import os
import csv

os.chdir(os.path.dirname(os.path.abspath(__file__)))
election_csv = os.path.join("election_data.csv")

Total_Votes = 0
Candidate_Kahn = 0
Candidate_Correy = 0
Candidate_Li= 0
Candidate_OTooley = 0
candidate_votes = {}
cand_vote_percent = {}
Winner_Votes = 0
Winner = ""

with open(election_csv) as csvfile:
     csvreader = csv.reader(csvfile, delimiter=",")
     csv_header =next(csvreader)
     print (csv_header)

     for row in csvreader:
          
          Total_Votes = Total_Votes + 1
          candidate = row[2]
         
          if candidate in candidate_votes:
               candidate_votes[candidate] = candidate_votes[candidate] + 1
          else: candidate_votes[candidate] = 1

for person, vote_count in candidate_votes.items():
     cand_vote_percent[person] = '{0:.0%}'.format(vote_count / Total_Votes)
     if vote_count > Winner_Votes:
          Winner_Votes = vote_count
          winner = person
dashbreak = "-------------------------"  
print("Election Results")
print(dashbreak)
print(f"Total Votes: {Total_Votes}")
print(dashbreak)
for person, vote_count in candidate_votes.items():
     print(f"{person}: {cand_vote_percent[person]} ({vote_count})")
print(dashbreak)
print(f"Winner: {winner}")
print(dashbreak)

