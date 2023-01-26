# Import os module to create file path across operating systems
import os

# Module for reading csv files
import csv

# Module for statistics
import statistics

# Path to csv
budget_data_csv = os.path.join(os.path.dirname(os.path.abspath( __file__)), 'resources', 'budget_data.csv')

# Define variables
monthCount = 0
totalVolume = 0
greatestIncrease = 0
bestMonth = ' '
greatestDecrease = 0
worstMonth = ' '

change = []
monthToMonthChange = []

# Functions
with open(budget_data_csv, newline='') as csvfile:
    
    # CSV reader  that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Read first row header.  Skip if none. 
    csv_header =next(csvreader)
    # print(f"CSV Header: {csv_header}")
    
    # Read each row of data after the header
    for row in csvreader:
        #print(row)
        monthCount += 1
        totalVolume = int(row[1])
        if int(row[1]) > greatestIncrease:
            bestMonth = (row[0])
            greatestIncrease = int(row[1])
        elif int(row[1]) < greatestDecrease:
            worstMonth = (row[0])
            greatestDecrease = int(row[1])
        change.append(int(row[1]))
        
    # Track monthly changes
    for i in range(len(change)-1):
        monthlyChange = (change[i+1] - change[i])
        monthToMonthChange.append(monthlyChange)
        
    averageChange = statistics.mean(monthToMonthChange)
     
    # Output
    print("Financial Analysis")
    print("--------------------------------")
    print("Total Months: " + str(monthCount))

    print("Average Change is: $" + str(round(averageChange, 2)))
    print("Total: $" + str(totalVolume))
    print("Greatest Increase in Profits: " + str(bestMonth) + "  ($" + str(greatestIncrease) + ")")
    print("Greatest Decrease in Profits: " + str(worstMonth) + "  ($" + str(greatestDecrease) + ")")

    # Write to an output file
    f = open("financial_analysis.txt", "w")
    f.write("Financial Analysis")
    f.write("___________________________________")

    f.write("Total Months: " + str(monthCount))
    f.write("Average Change is: $" + str(round(averageChange, 2)))
    f.write("Total: $" + str(totalVolume))
    f.write("Greatest Increase in Profits: " + str(bestMonth) + "  ($" + str(greatestIncrease) + ")")
    f.write("Greatest Decrease in Profits: " + str(worstMonth) + "  ($" + str(greatestDecrease) + ")")

    # Secondary output text file detailing where to find the output text within the python-challenge folder
    text_file =open('python-challenge.txt', 'w')
    text_file.write('PyBank output has been exported as a file named "financial_analysis.txt" within the PyBank folder of this repository. I have also placed a copy in the "Analysis" folder within PyBank as per the instructions for this assignment. ')
    text_file.close() 
                   

    