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
net_profit_loss = 0
PrevMonthLoss =0
CurrentMonthLoss =0
ProfitChange =0
totalVolume = 0
GreatestIncrease = 0
BestMonth = ' '
GreatestDecrease = 0
WorstMonth = ' '

#monthToMonthChange = []
months =[]
ProfitLossChanges = []
MonthToMonthChange = []

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
        # totalVolume = int(row[1])
        # if int(row[1]) > greatestIncrease:
        #     bestMonth = (row[0])
        #     greatestIncrease = int(row[1])
        # elif int(row[1]) < greatestDecrease:
        #     worstMonth = (row[0])
        #     greatestDecrease = int(row[1])
        # change.append(int(row[1]))
        
        # Determine Profit/Loss for entire period
        CurrentMonthLoss = int(row[1])
        net_profit_loss += CurrentMonthLoss
        
        # Set value of previous month to equal the current month
        if(monthCount ==1):
            PrevMonthLoss =CurrentMonthLoss
            continue
        
        # Calculate for change in profit loss
        else:
            ProfitChange = CurrentMonthLoss - PrevMonthLoss
            
            # Add each month to total
            months.append(row[0])
            
            # Apprend each profit loss to month to month changes 
            ProfitLossChanges.append(ProfitChange)
            
            # Make current month loss equal to previous month loss
            PrevMonthLoss=CurrentMonthLoss
            
    # Get total and average changes in profit losses over the entire period
    SumProfitLoss =sum(ProfitLossChanges)
    AverageChange = round(SumProfitLoss/(monthCount -1), 2)
    
    # Find highest and lowest changes for entire period
    GreatestIncrease = max(ProfitLossChanges)
    GreatestDecrease = min(ProfitLossChanges)
    
    # Find index value of highest and lowest changes
    HighestMonthIndex = ProfitLossChanges.index(GreatestIncrease) 
    LowestMonthIndex = ProfitLossChanges.index(GreatestDecrease)
    
    # Determine best and worth month(s)
    BestMonth = months[HighestMonthIndex]
    WorstMonth = months[LowestMonthIndex]
    
# Print 
print("Financial Analysis")
print("----------------------------")
print("Total Months: " + str(monthCount))
print("Average Change is: $" + str(round(AverageChange, 2)))
print("Total: $" + str(net_profit_loss))
print("Greatest Increase in Profits: " + str(BestMonth) + "  ($" + str(GreatestIncrease) + ")")
print("Greatest Decrease in Profits: " + str(WorstMonth) + "  ($" + str(GreatestDecrease) + ")")

    
    # Track monthly changes
for i in range(len(ProfitLossChanges)-1):
    monthlyChange = (ProfitLossChanges[i+1] - ProfitLossChanges[i])
    MonthToMonthChange.append(monthlyChange)
        
    AverageChange = statistics.mean(MonthToMonthChange)
     


    # Write to an output file
    financial_analysis = os.path.join("Analysis", "financial_analysis.txt")
    with open(financial_analysis, "w") as output:
        output.write("Financial Analysis\n")
        output.write("-------------------------\n")
        output.write("Total Months: " + str(monthCount))
        output.write("\n-----------------------------------\n")
        output.write("Average Change is: $" + str(round(AverageChange, 2)))
        output.write("\n------------------------------------\n")
        output.write("Total: $" + str(net_profit_loss))
        output.write("\n------------------------------------\n")
        output.write("Greatest Increase in Profits: " + str(BestMonth) + "  ($" + str(GreatestIncrease) + ")")
        output.write("\n-------------------------------------\n")
        output.write("Greatest Decrease in Profits: " + str(WorstMonth) + "  ($" + str(GreatestDecrease) + ")")
        output.write("\n-------------------------------------\n")
    
        
 
    # f.write("Financial Analysis")
    # f.write("___________________________________")
    # f.write("Total Months: " + str(monthCount))
    # f.write("Average Change is: $" + str(round(AverageChange, 2)))
    # f.write("Total: $" + str(totalVolume))
    # f.write("Greatest Increase in Profits: " + str(BestMonth) + "  ($" + str(GreatestIncrease) + ")")
    # f.write("Greatest Decrease in Profits: " + str(WorstMonth) + "  ($" + str(GreatestDecrease) + ")")
    # # Output
    # print("Financial Analysis")
    # print("--------------------------------")
    # print("Total Months: " + str(monthCount))

    # print("Average Change is: $" + str(round(averageChange, 2)))
    # print("Total: $" + str(totalVolume))
    # print("Greatest Increase in Profits: " + str(bestMonth) + "  ($" + str(greatestIncrease) + ")")
    # print("Greatest Decrease in Profits: " + str(worstMonth) + "  ($" + str(greatestDecrease) + ")")
    #    f = open("financial_analysis.txt", "w")
   
   
    # Secondary output text file detailing where to find the output text within the python-challenge folder
    text_file =open('python-challenge.txt', 'w')
    text_file.write('PyBank output has been exported as a file named "financial_analysis.txt" within the PyBank folder of this repository. I have also placed a copy in the "Analysis" folder within PyBank as per the instructions for this assignment. ')
    text_file.close() 
                   

    