# Import modules
import os
import csv

# Initialize variables
row1 = 0
row2 = 0
change_month = 0
total_months = 0
net = 0

# Initialize lists to store data
date = []
profitLosses = []

# Create path to csv file
path = os.path.join('PyBank', 'Resources', 'budget_data.csv')

# Open the csv
with open(path) as csvfile:
    