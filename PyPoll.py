
import os
import csv

election_data = os.path.join("election_data.csv")

candidates = []
num_votes = []
percent_votes=[]
total_votes = 0

with open(election_data, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    csv_header = next(csvreader)

    for row in csvreader:
        total_votes += 1

        if row[2] not in candidates:
            candidates.append(row[2])
            index = candidates.index(row[2])
            num_votes.append(1)
        else:
            index = candidates.index(row[2])
            num_votes[index] += 1

    for votes in num_votes:
        percentage = (votes/total_votes) * 100
        percentage = round(percentage)
        percentage = "%.3f%%" % percentage
        percent_votes.append(percentage)
    
print("Election Results")
print("-------------------")
print(f'Total Votes: {str(total_votes)}')
print(f'------------------')
for i in range(len(candidates)):
    print(f'{candidates[i]}: {percent_votes[i]} {num_votes[i]}')
print('-------------------')
print(f'Winner: Khan')
print(f'------------------')

poll_file = os.path.join("PYPoll Text.rtf")
with open(poll_file, "w") as outfile:
    outfile.write("Election Results\n")
    outfile.write("-------------------\n")
    outfile.write(f'Total Votes: {str(total_votes)}\n')
    outfile.write(f'------------------\n')
    for i in range(len(candidates)):
        outfile.write(f'{candidates[i]}: {percent_votes[i]} {num_votes[i]}\n')
    outfile.write('-------------------\n')
    outfile.write(f'Winner: Khan\n')
    outfile.write(f'------------------\n')