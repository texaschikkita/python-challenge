# Import os module to create file path across operating systems
import os

# Module for reading csv files
import csv

# Module for statistics
import statistics

# Import Dictionary
from collections import defaultdict
     
# Path to csv
Pollelection_data_csv = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'resources', 'Pollelection_data.csv')


# Total Vote Counter
total_votes = 0

# Define lists and variables
candidate_options  = []
candidate_votes = {}
county_options = []
county_votes = {}

winning_candidate = ""
winning_count = 0
winning_county = 0
winning_percent = 0
winning_county_percent = 0
winning_county_candidate = ""
winning_county_summary = []



county_most_voters = ""
count_of_county_most_voters = 0

              
# Functions
with open(Pollelection_data_csv, newline='') as csvfile:
     
    # CSV reader  that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Read first row header.  Skip if none. 
    csv_header =next(csvreader)
    # print(f"CSV Header: {csv_header}")

# For each row in csv file
    for row in csvreader:
        # Add to total vote count
        total_votes = total_votes + 1
    
        # Get candidate name and county from rows
        candidate_name = row[2]
    
        # Get county name from rows
        county_name =row[1]
    
        # If it is a new unique name add it to candidate list
        if candidate_name not in candidate_options:
        
            # Add name to candidate list
            candidate_options.append(candidate_name)
            # Count candidate's votes
            candidate_votes[candidate_name] = 0
        
        # Add 1 vote to candidate's count
        candidate_votes[candidate_name] += 1
    
        # Verify the county does not match any existing county in county list
        if county_name not in county_options:
            # Add to list of counties
            county_options.append(county_name)
        
            # Count votes for county
            county_votes[county_name] = 0
    
        # Add a vote to county's vote count
        county_votes[county_name] += 1
    

election_results = (
        f"\n-------------------------\n"
        f"Election Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n\n"
        f"County Votes:\n")
print(election_results, end="")



# Loop for county_name in county_votes  
for county_name in county_votes:
    county =county_votes.get(county_name)
    
    # Float percent of total county votes
    county_percentage = float(county) / float(total_votes) * 100
    county_results = (
        f"{county_name}: {county_percentage:.1f}% ({county:,})\n")


    # Print results 
    print(county_results, end="")    
       
    # If statement to determine winning count
    if(county > winning_county) and (county_percentage > winning_county_percent):
        winning_county = county
        winning_county_candidate = county_name
        winning_county_percent = county_percentage
        
    
    # Print county with largest turnout
    winning_county_summary = (
        f"\n_______________________________________\n"
        f"County with the Biggest Turnout is : {winning_county_candidate}\n"        
        f"Winning County Vote: {winning_county:,}\n"
        f"\n_______________________________________\n")
    print(winning_county_summary)
    
    
    # Export final candidate vote count 
    for candidate_name in candidate_votes:
        # Calculate vote count and %
        votes = candidate_votes.get(candidate_name)
        vote_percentage  = float(votes) /float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        
    
        
    # Print total vote count for each candidate
    print(candidate_results)
   
    
    # Calculate winning vote count, % and candidate
    if (votes > winning_count)  and (vote_percentage > winning_percent):
        winning_count = votes
        winning_candidate = candidate_name
        winning_percent = vote_percentage
        
   
    # Print Results
    candidate_summary = (
        f"\n_______________________________________\n"
        f"{winning_candidate}: {winning_percent:.1f}:% {winning_count:,}\n)")
    print(candidate_summary)
    
# Export text file with results
text_file=open('election_results,txt', 'w')
text_file.write("Election Results ")
text_file.write(winning_county_summary)
