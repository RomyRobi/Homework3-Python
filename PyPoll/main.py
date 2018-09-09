# Import Dependencies
import os
import csv

# Create file path
csv_path = os.path.join("Resources", "election_data.csv")

# Open file as cvs file and skip headers
with open(csv_path, newline='') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ',')
    next(csv_reader)
    # Create counter/dictionary for total number of votes, candidates' votes, etc.
    count_votes = 0
    candidates_votes = {}
    winner = 0
    # Loop through each row of data
    for row in csv_reader:
        # If statement to add candidate and first vote to dictionary or tally votes
        if row[2] not in candidates_votes.keys():
            candidates_votes[row[2]] = 1
        else:
            candidates_votes[row[2]] += 1
        # Increase vote count for each row of data
        count_votes += 1
    # Open/create .txt file to write results to
    txt_file = open("PypollResults.txt", "w")
    # Print results to terminal and .txt file
    print("Election Results")
    print("---------------------------------")
    print(f'Total Votes: {count_votes}')
    print("---------------------------------")
    print("Election Results", file=txt_file)
    print("---------------------------------", file=txt_file)
    print(f'Total Votes: {count_votes}', file=txt_file)
    print("---------------------------------", file=txt_file)
    # Loop through dictionary to extract candidates and their votes and print
    for key, value in candidates_votes.items():
        if value > winner:
            winner = value
            winner_name = key
        percent_total = round((value/count_votes)*100, 3)
        print(f'{key}: {percent_total}% ({value})')
        print(f'{key}: {percent_total}% ({value})', file=txt_file)
    print("---------------------------------")
    print("---------------------------------", file=txt_file)
    print(f'Winner: {winner_name}')
    print(f'Winner: {winner_name}', file=txt_file)
    print("---------------------------------")
    print("---------------------------------", file=txt_file)
