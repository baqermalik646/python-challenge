import csv
import os
from collections import Counter

path = "/Users/muhammadbaqermalik/Desktop"
election_csv = os.path.join(path, 'DataScienceBootcamp', 'Homework', '03-Python', 'python-challenge','python-challenge', 'PyPoll', 'Resources', 'election_data.csv')

with open(election_csv, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    file_header = next(csvreader)
    candidates_list = []
    votesCount = Counter()
    percentage_of_votes = []
    election_results = []

    for row in csvreader:
        candidates_list.append(row[2])

    for candidate_name in candidates_list:
        votesCount[candidate_name] += 1

    winner_candidate = max(zip(votesCount.values(), votesCount.keys()))
    candidate_name = tuple(votesCount.keys())
    votes = tuple(votesCount.values())

    totalVotes = len(candidates_list)
    for k in votes:
        percentage_of_votes.append((int(k) / totalVotes) * 100)

    election_results.append("Election Results")
    election_results.append("---------------------")
    election_results.append('Total Votes: ' + str(totalVotes))
    election_results.append("---------------------")
    for m in range(len(candidate_name)):
        election_results.append(candidate_name[m] + ': ' + str(round(percentage_of_votes[m], 3)) + '% ' + '(' + str(votes[m]) + ')')
    election_results.append("---------------------")
    election_results.append('Winner: ' + winner_candidate[1])
    election_results.append("---------------------")

    print("\n".join(election_results))


path = "/Users/muhammadbaqermalik/Desktop"
output_file = os.path.join(path, 'DataScienceBootcamp', 'Homework', '03-Python', 'python-challenge','python-challenge', 'PyPoll', 'analysis', 'Election Results.txt')


with open(output_file, "w") as file:
        file.write("\n".join(election_results))
