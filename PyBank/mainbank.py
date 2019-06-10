# Modules
import csv

# Set path for file
csvpath = "budget_data.csv"

with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Read the header row first 
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    first_row = next(csvreader)

    count = 1 # The adds the first row that was not included
    PL_total = int(first_row[1]) #Adding back in first value to the total PL
    changes = [] #Adds a list of numbers that are the difference between one month and the next
    firstPL = int(first_row[1])
    
    # Read each row of data after the header
    for row in csvreader:
        #print(row) - this will give a cumulative monthly total
        count += 1 # Count months
        PL_total = int(row[1]) + PL_total #Starts from row 3
        net_change = int(row[1]) - firstPL #
        firstPL = int(row[1]) #Resets the value of FirstPl to the
        changes.append(net_change)
        max_month = max(changes)
        least_mth = min(changes)
        avg_change = sum(changes) / len(changes)

    print("Financial Analysis")
    print('--------------------------------')
    print(f"The number of months are {count}")
    #print(f"Net change is {changes}")
    print(f'The total Profits and Loss are {PL_total}')
    print(f'The average change in profit is {avg_change}')
    print(f'The greatest increase in profits is from {max_month}')
    print(f'The greatest loss was {least_mth}')