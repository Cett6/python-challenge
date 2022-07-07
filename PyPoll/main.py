import os

import csv

election_data_in = os.path.join("Resources", "election_data.csv")
election_data_out = os.path.join("analysis", "election_data_analysis.txt")


totalvotes= 0

totalnet=0

with open(election_data_in,"r") as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=",")
    
    Headers = next(csvreader)

    firstrow=next(csvreader)
    totalvotes = totalvotes + 1
    totalnet += int(firstrow[0])
    previousnet=int(firstrow[0])

    candidateList = []

    Stockham_Votes = 0
    Degette_Votes = 0
    Doane_Votes = 0 

    for row in csvreader:
        totalvotes += 1
        
        candidates = row[2]
       # candidateList.append(candidates)
        if not candidates in candidateList:
            candidateList.append(candidates)

        if row[2]=="Charles Casper Stockham":
            Stockham_Votes += 1
        elif row[2] == "Diana DeGette":
            Degette_Votes += 1
        elif row[2] == "Raymon Anthony Doane":
            Doane_Votes += 1
        else:
            pass
   # candidateList = list(set(candidateList))

    #Vote totals
    Stockham_Votes_Percent = (Stockham_Votes / totalvotes) * 100
    Degette_Votes_Percent = (Degette_Votes / totalvotes) * 100
    Doane_Votes_Percent = (Doane_Votes / totalvotes) * 100


 #using if/and statements to calculate a winner
    Winner = 0
    if Stockham_Votes_Percent > Degette_Votes_Percent and Doane_Votes_Percent:
        Winner = "Charles Casper Stockham"
    elif Degette_Votes_Percent > Stockham_Votes_Percent and Doane_Votes_Percent:
        Winner = "Diana DeGette"
    elif Doane_Votes_Percent > Stockham_Votes_Percent and Degette_Votes_Percent:
        Winner = "Raymon Anthony Doane"



output = (
    
    f"\nElection Results\n"
    f"-------------------------\n"
    f"Total Votes: {totalvotes}\n"
    f"-------------------------\n"
    f"Charles Casper Stockham: {Stockham_Votes_Percent:,.3f}% ({Stockham_Votes})\n"
    f"Diana Degette: {Degette_Votes_Percent:,.3f}% ({Degette_Votes})\n"
    f"Raymon Anthony Doane: {Doane_Votes_Percent:,.3f}% ({Doane_Votes})\n"
    f"-------------------------\n"
    f"Winner: {Winner}\n"
    f"-------------------------\n"

    
)
print(output)
with open(election_data_out, 'w') as txtfile:
    txtfile.write(output)
