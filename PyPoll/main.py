import os
import csv

# Path to collect data from the Resources folder
election_csv = os.path.join ('Resources', 'election_data.csv')

ballot = []
county = []
candidates = []

# Read the CSV file
with open(election_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)

    # loop through each row of the file to get data sorted into different variables
    for row in csvreader:

        ballot.append(row[0])
        county.append(row[1])
        candidates.append(row[2])

    # Calculate total number of votes
    total_votes = len(ballot)
    print(f'Total votes: {total_votes}')

    # Complete list of candidtes who received votes
    unique_values = set(candidates) 
    unique_candidates = (list(unique_values))
            
    # Number of votes for each candidate 
    cand1 = 0
    cand2 = 0
    cand3 = 0

    # Loop through candidates and sum the number of votes for each
    for cand in candidates:
        if cand == unique_candidates[0]:
            cand1 = cand1+1
        elif cand == unique_candidates[1]:
            cand2 = cand2+1
        else:
            cand3 = cand3+1

    # The percentage of votes each candidate won
    per_cand1 = round(cand1/total_votes*100,3)
    per_cand2 = round(cand2/total_votes*100,3)
    per_cand3 = round(cand3/total_votes*100,3)

    print(f'{unique_candidates[0]}: {per_cand1}% ({cand1})')
    print(f'{unique_candidates[1]}: {per_cand2}% ({cand2})')
    print(f'{unique_candidates[2]}: {per_cand3}% ({cand3})')

    # The winner of the election based on popular vote
    max_votes = max(cand1, cand2, cand3)
    if max_votes == cand1:
        winner = unique_candidates[0]
    elif max_votes == cand2:
        winner = unique_candidates[1]
    else:
        winner == unique_candidates[2]

    print(f'Winner: {winner}')

    # Write text file
    output_path = os.path.join ('analysis', 'pypoll.txt')

    with open(output_path, 'w') as text:
        text.write ('Election results \n'
                    '---------------------------------- \n'
                    f'Total votes: {total_votes} \n'
                    '---------------------------------- \n'
                    f'{unique_candidates[0]}: {per_cand1}% ({cand1}) \n'
                    f'{unique_candidates[1]}: {per_cand2}% ({cand2}) \n'
                    f'{unique_candidates[2]}: {per_cand3}% ({cand3}) \n'
                    '---------------------------------- \n'
                    f'Winner: {winner} \n'
                    '----------------------------------')

    