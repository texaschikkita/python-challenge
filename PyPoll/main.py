import csv
from distutils import text_file
from itertools import count
import os

# Assign a variable to load and write to a file from a path.
file_to_load = os.path.join("Resources", "election_data.csv")
file_to_output=os.path.join("analysis", "election_results.txt")

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
winning_county = ""
winning_county_count = 0
winning_county_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # Read and analyze the data here.
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:
        
        # Run leader animation
        print(".  ", end=""),
        
        # Add to the total vote count.
        # total_votes = total_votes + 1 (long format)
        total_votes += 1  #shorter way to write the same line 
        
        # Note select lines then hit ctrl+'/?' for shortcut to comment out section 
    
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
      
        
         # Loop through counts to determine winner 
    for candidate in candidate_votes:
        # Retrieve vote count of a candidate.
     
        # Calculate the percentage of votes.
        votes = candidate_votes.get(candidate)                                                          
        vote_percentage =float(votes) / float(total_votes) * 100                                
        
          
        # Determine winning vote count and candidate
        if  (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate                                                              
        
        # Print the candidate name and percentage of votes.
        voter_output = f"\n{candidate}: {vote_percentage:.3f}% ({votes})\n"
        print(voter_output,  end="")   
        
#Create output report
with open(file_to_output, "w") as txt_file:

    # Print final vote count to terminal
    election_results = (
        f"\n\nElection Results\n"
        f"__________________________\n"
        f"Total Votes:  {total_votes}\n"
        f"__________________________\n"
        )
    print(election_results, end="")


# Print the winning candidate's results.
winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)

# Create output report
with open(file_to_output, "w") as txt_file:

    # Print final vote count to terminal
    election_results = (
        f"\n\nElection Results Per County\n"
        f"__________________________\n"
        f"Total Votes:  {total_votes}\n"
        f"__________________________\n"
        )
    print(election_results, end="")
    

with open(file_to_output, "w") as txt_file:
    txt_file.write(winning_candidate_summary)
        
    #   Loop through counties to determine vote percentage for counties.
    for county_name in county_list:
        
        # Retrieve county name
        #county_vote =county_votes.get(county)
        county_vote = county_votes.get(county_name)
        
        # Float percentage of total county votes
        county_percentage = float(county_vote) / float(total_votes) * 100
        
   
        # Determine which county had the winning count/largest voter turnout
        if (county_vote > winning_county_count) and (county_percentage > winning_county_percentage):
            winning_county_count = county_vote
            winning_county_percentage = county_percentage
            winning_county = county_name   
                
                
  
        county_output = f"{county_name}: {county_percentage:.3f} ({county_vote:,})\n"  #see for change
        print(county_output, end="")

        
# Print county with largest turnout
winning_county_summary = (
    f"\n---------------------------\n"
    f"Largest County Turnout: {winning_county}\n"
    f"Largest County Vote Count: {winning_county_count:,}\n"
    f"Largest County Vote Percentage: {winning_county_percentage:.1f}%\n"       
    f"----------------------------\n")
print(winning_county_summary)


        
# Write to output file
with open (file_to_output, "w") as txt_file:
    txt_file.write(winning_county_summary)


# election_results = (
#     f"Election Results\n"
#     f"____________________\n"
#     f"Total Votes:\n"
#     f"____________________\n"
#     )
# print(election_results)


 # Print candidate's voter count and percentage to text file                               
with open (file_to_output, "w") as txt_file:
    txt_file.write(voter_output)
    txt_file.write(election_results) 
     
     