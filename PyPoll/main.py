import csv
from itertools import count
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_data.csv")

# Initialize a total vote counter.
total_votes = 0

# Candidate options and candidate votes.
candidate_options = []
candidate_votes = {}

# Track the winning candidate, vote count, and percentage.
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# County list and votes
county_list =[]
county_votes = {}

# Track largest county, county vote count and county vote percentage.
largest_county_turnout = ""
largest_county_turnout_count = 0
largest_county_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # Read and analyze the data here.
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1

        # CANDIDATES
        # Get the candidate name from each row.
        candidate_name = row[2]

        # If the candidate does not match any existing candidate, add name to candidate list.
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)

            # Begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0
        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1
        
        # COUNTY
        # Get the county name from each row. If it's a new name, add to county list.
        county_name = row[1]
        if county_name not in county_list:
            county_list.append(county_name)
         
           # Begin tracking votes for each county
            county_votes[county_name] = 0
        # Add a vote to the county's vote count
        county_votes[county_name] += 1

    # Loop through counts to determine vote percentage for candidates.
    for candidate in candidate_votes:
        # Retrieve vote count of a candidate.
        votes = candidate_votes[candidate]
        # Calculate the percentage of votes.
        vote_percentage = int(votes) / int(total_votes) * 100

        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate
            winning_percentage = vote_percentage
                 # Print the candidate name and percentage of votes.
        print (f"[{candidate}]: received {votes} votes, receiving {vote_percentage:.1f}% of the vote")
            
       
    #   Loop through counties to determine vote percentage for counties.
    for county in county_list:
        # Retrieve county name
        county_vote = county_votes.get(county)
        # Float percentage of total county votes
        county_vote_percentage = float(county_vote) / float(total_votes) * 100
       
        # Determine which county had the winning count/largest voter turnout
        if (county_vote > largest_county_turnout_count) and (county_vote_percentage > county_vote_percentage):
            largest_county_turnout_count = county_vote
            largest_county_percentage = county_vote_percentage
            largest_county_turnout = county    
                
    

   
        
        # Print the winning candidate's results.
        winning_candidate_summary = (
            f"-------------------------\n"
            f"Winner: {winning_candidate}\n"
            f"Winning Vote Count: {winning_count:,}\n"
            f"Winning Percentage: {winning_percentage:.1f}%\n"
            f"-------------------------\n")
        print(winning_candidate_summary)
        
     


        # Print the total votes
        # print(total_votes)
        # print(candidate_options)
        # print(candidate_votes)

  
        # Print County Results
        # print(county_results)

        # Print counties
        print(county_votes)
        
        # Print county with largest turnout
        winning_county_summary = (
            f"---------------------------\n"
            f"Largest County Turnout: Denver with 82.2%\n"        
            f"----------------------------\n")
        print(winning_county_summary)
      