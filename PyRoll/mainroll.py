# Modules
import csv

# Set path for file
csvpath = "election_data.csv"

#Set variables
candidate = []
total_votes = {}
count = 0
with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first 
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

     #Method 1   
    for row in csvreader:
        #print(row) - this will give a cumulative monthly total
        count += 1 # Count ballots
        candidate_name = str(row[2])
        if candidate_name not in candidate:
            candidate.append(candidate_name)

    #Method 2
        if candidate_name in total_votes:
          total_votes[candidate_name]+=1
        else:
          total_votes[candidate_name] = 1
    
print("Election Results")
print('--------------------------------')
print(f"The total votes are {count}")
print('--------------------------------')
print(f"The list of candidates are {candidate}")

winner = ""
winner_vote = 0

for elector in total_votes:
    #100*total_votes[elector]/float(count)
    print (elector+":", "{:.2f}".format(100*total_votes[elector]/float(count)), "%", "(", total_votes[elector],")")
    if total_votes[elector]>winner_vote:
        winner = elector
        winner_vote = total_votes[elector]
print('--------------------------------')      
print(f"The winner of the election is {winner}")
print('--------------------------------')