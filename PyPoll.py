# The data we need to retrieve.
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the electiopn based on popular vote.

# Add our dependencies.

import csv

import os

# Assign a variable to load a file from a path.

file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a variable to save the file to a path.

file_to_save = os.path.join("analysis", "election_analysis.txt")

# Add total vote counter before with open()

total_votes = 0

#Print candidate name from each row

candidate_options = []

# Declare empty dictionary

candidate_votes = {}

# Open the election results and read the file.

# Winning Candidate and Winning Count Tracker

winning_candidate = ""
winning_count = 0
winning_percentage = 0

with open(file_to_load) as election_data:

    file_reader = csv.reader(election_data)

    
    headers = next(file_reader)

    for row in file_reader:

        

        total_votes += 1

        candidate_name = row[2]

        if candidate_name not in candidate_options:

            candidate_options.append(candidate_name)

            candidate_votes[candidate_name] = 0

        candidate_votes[candidate_name] += 1


    for candidate_name in candidate_votes:

        votes = candidate_votes[candidate_name]

        vote_percentage = float(votes) / float(total_votes) * 100

        print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        if (votes > winning_count) and (vote_percentage > winning_percentage):
    
            winning_count = votes

            winning_percentage = vote_percentage
            
            winning_candidate = candidate_name

    winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")

    print(winning_candidate_summary)


    print(f"{candidate_name}: received {vote_percentage}% of the vote.")



print(candidate_votes)



