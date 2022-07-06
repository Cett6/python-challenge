
import os

import csv
from signal import getsignal
import statistics

budget_data_in = os.path.join("Resources", "budget_data.csv")
budget_data_out = os.path.join("analysis", "budget_analysis.txt")
print("Financial Analysis")
print(" ")
print("----------------------------------")
print(" ")

totalmonths= 0
monthofchange = []

netchangelist=[]
totalnet=0


with open(budget_data_in, 'r') as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=",")
    
    #print(csvreader)
    
    Headers = next(csvreader)

    #print(Headers)
    firstrow=next(csvreader)
    totalmonths = totalmonths + 1
    totalnet += int(firstrow[1])
    previousnet=int(firstrow[1])


    for row in csvreader:
        totalmonths += 1
        #print(("Total Months: "), (totalmonths-1))
        totalnet += int(row[1])
        netchange= int(row[1]) - previousnet
        previousnet = int(row[1])
        
        
        netchangelist += [netchange]
        monthofchange+=[row[0]]
    
    #averagechange =statistics.mean(row[1])
    
    gincrease=[]
    gdecrease=[]
    
    for row in csvreader:
        gincrease=row[0], gincrease.append(max(row[1]))
        gdecrease=row[0], gdecrease.append(min(row[1]))
    

    
output = (
    f"Financial Analysis\n"
    f"----------------------------\n"
    f"Totalmonths:{totalmonths}\n"
    f"Total: ${totalnet}\n"
   # f"Average Change: ${averagechange}\n"
    f"Greatest increase in profits: {gincrease}\n"
    f"Greastes decrease in profits: {gdecrease}\n"
    
)
print(output)
with open(budget_data_out, 'w') as txtfile:
    txtfile.write(output)

