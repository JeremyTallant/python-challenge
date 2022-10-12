#print financial analysis and a line in the terminal
print("Financial Analysis\n")

print("-------------------------------\n")

#import the modules to allow us to create file paths across operating systems and for reading csv files
import os

import csv

#create a path to the csv file with a variable 
the_path = os.path.join('Resources', 'budget_data.csv') 

#create lists to store data
Date = []
ProfitLosses = []

#open then csv file
with open(the_path) as csvfile:
    
    #use the csvreader to specify the delimiter and variable that holds contents 
    csvreader = csv.reader(csvfile, delimiter=',')

    #read the header row first 
    csvheader = next(csvreader)

    #establish default amounts for variables 
    row1 = 0
    row2 = 0
    change_month = 0
    totalmonths = 0
    net = 0

    #start loop to read each row of data after header 
    for row in csvreader:

        #find the total number of months in the data
        totalmonths += 1

        #find the net total amount of "Profit/Losses" over the entire period
        net += int(row[1])

        #define row1 as an integer
        row1 = int(row[1])

        #find the changes in "Profit/Losses" over the entire period with an if/else statement
        if (totalmonths==1):
            row2 =row1
        
        else:
            change_month = row1 - row2
            Date.append(row[0])
            ProfitLosses.append(change_month)
            row2 = row1

    #find the average of the changes in "Profit/Losses" over the entire period
    average = round(sum(ProfitLosses)/(totalmonths-1), 2)

    #find the amount of the greatest increase and decrease in profits over the entire period
    gi = max(ProfitLosses)
    gd = min(ProfitLosses)

    #find the date of the greatest increase and decrease in profits over the entire period  
    gid = Date[ProfitLosses.index(gi)]
    gdd = Date[ProfitLosses.index(gd)]

#print the results in the terminal 
print(f"Total Months: {totalmonths}\n")
print(f"Total: ${net}\n")
print(f"Average Change: ${average}\n")
print(f"Greatest Increase in Profits: {gid} (${gi})\n")
print(f"Greatest Decrease in Profits: {gdd} (${gd})\n")

#set the variable for the results to be printed in a txt file 
results = ('Analysis/results.txt')

#open the text file and write the results 
with open(results, "w") as text:
    text.write("Financial Analysis\n")
    text.write("-------------------------------\n") 
    text.write(f"Total Months: {totalmonths}\n")
    text.write(f"Total: ${net}\n")
    text.write(f"Average Change: ${average}\n")
    text.write(f"Greatest Increase in Profits: {gid} (${gi})\n")
    text.write(f"Greatest Decrease in Profits: {gdd} (${gd})\n")
