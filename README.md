# Automating with Python

![image](images/python.png)

## Background
This project signifies a pivotal shift from conventional data analysis methods to advanced programming techniques using Python. It encompasses two challenges - PyBank and PyPoll - designed to apply Python scripting skills in real-world-like scenarios.

In the PyBank challenge, the focus is on automating financial analysis. The task involves scripting in Python to process and analyze a dataset comprising financial records, specifically to compute critical financial metrics and extract meaningful insights from them.

The PyPoll challenge, on the other hand, is centered around election data analysis. It involves developing a Python script to efficiently count votes, analyze electoral results, and provide comprehensive insights into the voting patterns and outcomes.

Both challenges serve as a practical application of Python in data processing and analytics, emphasizing the language's flexibility and power in handling diverse types of data. This project not only enhances Python programming skills but also provides a deeper understanding of how these skills can be applied in real-world data analysis scenarios.
## Objective
The primary objective of this project is to develop and demonstrate proficiency in Python programming through two distinct, real-world challenges: PyBank and PyPoll.

### PyBank Objective:
* **Develop a Python Script**: Create a script that efficiently analyzes financial data.
* **Analyze Financial Records**: Work with `budget_data.csv` to calculate key financial metrics.
* **Deliver Key Insights**: Determine total months covered, net total of "Profit/Losses", average changes in "Profit/Losses", and pinpoint the greatest increases and decreases in profits.
* **Generate Reports**: The script should output the analysis both in the terminal and as a text file, providing a clear, concise financial summary.
### PyPoll Objective:
* **Create a Vote-Counting Process**: Build a Python script to modernize and automate the vote-counting for a small town.
* **Analyze Election Data**: Utilize `election_data.csv` to calculate total votes, individual candidate performance, and election winner.
* **Summarize Election Results**: Present a detailed summary of each candidate's vote count and percentage, and declare the election winner.
* **Output Results**: The script should display the election results on the terminal and export them to a text file for record-keeping and easy dissemination.

The overall goal is to apply Python's powerful data manipulation capabilities to solve practical problems, showcasing how programming can be an invaluable tool in diverse areas such as finance and local governance. Through these challenges, the project aims to solidify foundational Python skills while also demonstrating the ability to handle real-world data sets effectively.
## Data
The data for this project was generated by edX Boot Camps LLC, and is intended for educational purposes only.
### PyBank Dataset
The PyBank challenge uses the `budget_data.csv` file, containing two columns:
* **Date**: This column records the month and year for each financial entry, reflecting the period of the financial data. 
* **Profit/Losses**: It shows the company's profit or loss for each month. 

Each row in the dataset represents a unique monthly record, combining to give a comprehensive view of the company's financial trajectory over the period covered by the dataset.

### PyPoll Dataset
For the PyPoll challenge, we'll use the `election_data.csv`, structured with three columns:
* **Voter ID**: A unique identifier for each voter, ensuring the integrity and tracking of individual votes.
* **County**: This column indicates the geographical location where the vote was cast.
* **Candidate**: It list the candidate's name for whom the vote was cast.

Each row in this dataset represents an individual vote, contributing to the overall analysis of the election results, including vote counts, candidate popularity, and voting demographics. 
## Implementation
### PyBank
The following section provides a detailed walkthrough of the Python script implemented for the PyBank challenge. This script is designed to analyze financial data and extract key metrics such as total months, net total profit/losses, and identifying significant fluctuations in profits.
#### Importing Modules
```python
# Import modules
import os
import csv
```
Initially, the script imports necessary modules - `os` for handling file paths and `csv` for reading CSV files.
#### Initializing Variables for Analysis
```python
# Initializing variables for analysis
total_months = 0
net_total = 0
monthly_changes = []
dates = []
```
Variables and lists are initialized here for tracking the total number of months (`total_months`), the net total amount of profit/losses (`net_total`), and storing monthly changes in profit/losses (`monthly_changes`) and their corresponding dates (`dates`). 
#### Setting the File Path and Reading the CSV
```python
# Path to the CSV file
csv_path = os.path.join('PyBank', 'Resources', 'budget_data.csv')

# Processing the CSV file
with open(csv_path, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Skip the header
    next(csvreader)
```
The path to the CSV file is defined, and the file is opened for reading. The `csv.reader` is used to parse the file, and `next(csvreader)` skips the header row.
#### Processing the CSV Data
```python
  # Read the first row to initialize variables
    first_row = next(csvreader)
    total_months = 1
    net_total = int(first_row[1])
    previous_amount = int(first_row[1])

    # Iterating over each row in the CSV
    for row in csvreader:
        # Tracking the total months and net total
        total_months += 1
        current_amount = int(row[1])
        net_total += current_amount

        # Calculating the monthly change and storing it
        change = current_amount - previous_amount
        monthly_changes.append(change)
        dates.append(row[0])

        # Updating the previous amount for the next iteration
        previous_amount = current_amount
```
The script reads the first data row to initialize the analysis. Then, a `for` loop iterates over each row in the CSV. In each iteration, it updates the total months and net total. It calculates the change in profit/losses compared to the previous month and stores this data along with the corresponding date.
#### Calculating Key Financial Metrics
```python
# Calculating average change, greatest increase and decrease
average_change = round(sum(monthly_changes) / len(monthly_changes), 2)
greatest_increase = max(monthly_changes)
greatest_decrease = min(monthly_changes)
```
After processing the data, the script calculates the average monthly change, the greatest increase, and the greatest decrease in profits.
#### Identifying Dates for Extremes in Profit/Losses
```python
# Dates of greatest increase and decrease
greatest_increase_date = dates[monthly_changes.index(greatest_increase)]
greatest_decrease_date = dates[monthly_changes.index(greatest_decrease)]
```
The dates associated with the greatest increase and decrease in profits are identified using the indices of the maximum and minimum values in `monthly_changes`.
#### Outputting the Results
```python
# Printing the financial analysis
print("Financial Analysis\n")
print("-------------------------------\n")
print(f"Total Months: {total_months}\n")
print(f"Total: ${net_total}\n")
print(f"Average Change: ${average_change}\n")
print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})\n")
print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})\n")

# Writing the results to a text file
results_path = os.path.join('PyBank', 'Analysis', 'results.txt')
with open(results_path, "w") as text_file:
    text_file.write("Financial Analysis\n")
    text_file.write("-------------------------------\n")
    text_file.write(f"Total Months: {total_months}\n")
    text_file.write(f"Total: ${net_total}\n")
    text_file.write(f"Average Change: ${average_change}\n")
    text_file.write(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})\n")
    text_file.write(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})\n")
```
Finally, the script prints the analysis results to the terminal and writes them to a text file. This ensures that the results are easily accessible both during runtime and for later reference.