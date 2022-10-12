#print election results and a line in the terminal 
print("Electon Results\n")

print("--------------------------\n")

#import the modules to allow us to create file paths accross operating systems and reading csv files
import os 

import csv

#create a path to the csv file with a variable
the_way = os.path.join('PyPoll', 'Resources', 'election_data.csv')

#create lists to store data
Votes = []
Candidates = []
Percentage = []

#open the csv file
with open(the_way) as csvfile:

    #use the csvreader to specify the delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    #read the header row first
    csvheader = next(csvreader)

    #establish default amount for variable
    totalvotes = 0 

    #start loop to read each row of data after header 
    for row in csvreader:

        #find the total number of votes cast
        totalvotes += 1

        #find the complete list of candidates who received votes and the total number of votes each candidate won 
        if row[2] not in Candidates:
            Candidates.append(row[2])
            index = Candidates.index(row[2])
            Votes.append(1)
        else:
            index = Candidates.index(row[2])
            Votes[index] += 1

     #find the winner of the election based on popular vote
    Winner = max(Votes)
    index = Votes.index(Winner)
    first_place = Candidates[index]

     #find the percentage of votes each candidate won
    for candidate_votes in Votes:
        Percent = round((candidate_votes / totalvotes) * 100, 3)
        Percentage.append(str(Percent) + "%")

#print the results in the terminal 
print(f"Total Votes: {totalvotes}\n")
print("--------------------------\n")
for i in range(len(Candidates)):
    print(f"{Candidates[i]}: {Percentage[i]} ({str(Votes[i])})\n")
print("--------------------------\n")
print(f"Winner: {first_place}\n")
print("--------------------------\n")

#set the variable for the results to be printed in a text file 
results = ('PyPoll/Analysis/results.txt')

#open the text file and write the results
with open(results, "w") as text: 
    text.write("Electon Results\n")
    text.write("--------------------------\n")
    text.write(f"Total Votes: {totalvotes}\n")
    text.write("--------------------------\n")
    for i in range(len(Candidates)):
        text.write(f"{Candidates[i]}: {Percentage[i]} ({str(Votes[i])})\n")
    text.write("--------------------------\n")
    text.write(f"Winner: {first_place}\n")
    text.write("--------------------------\n")