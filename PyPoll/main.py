# Import os module to create file path across operating systems
import os

# Module for reading csv files
import csv

    
# Path to csv
election_data_csv = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'resources', 'election_data.csv')


#election_data_csv = os.path.join("..", "Resources", "election_data.csv")

with open (election_data_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=' ')
    
    
    # Read header row fist
    csv_header =next(csvreader)
    #print(f"Header: {csv_header}")


    
    # Initialize Total Vote Counter
    total_votes = 0

    # Add candidate options and votes to dictionary
    candidate_options = []
    candidate_votes = {}


    # Add county list and county votes to dictionary 
    county_list =[]
    county_votes = {}

    # Define to track winning candidate, vote count and percentage
    winning_candidate = ""
    winning_count = 0
    winning_county = 0
    winning_percentage = 0

    # Define to track county with largest voter turnout
    # String to hold name of the county with the largest voter turnout
    largest_turnout_county = ""
    # Integers to hold the number of votes and % of votes for the county with the largest voter turnout
    turnout_votes = 0
    turnout_percentage = 0

    # Begin loop 
    for row in csvreader:
        total_votes = total_votes + 1
        

    # Get candidate name and county from rows
    candidate_name = row[2]
    county_name = row[1] 
    
    # If candidate name doesn't match an existing candidate name in list, add it
    if candidate_name not in candidate_options:
        candidate_options.append(candidate_name)
    
        # Begin counting thier votes
        candidate_votes[candidate_name] = 0
    
    # Add a vote to their vote count
    candidate_votes[candidate_name] =+ 1

     
    if county_name not in county_list:
        county_list.append(county_name)
        # Begin tracking votes per county
        county_votes[county_name] = 0
    
    # Add a vote to county's vote count
    county_votes[county_name] += 1


    # Print the vote count 
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n"
        f"County Votes:\n")
    print(election_results, end="")

  


    # Loop for county name 
    for county_name in county_votes:
        votes = county_votes.get(county_name)
        #  Calculate vote % for county
        vote_percentage = float(votes) / float(total_votes) * 100
        
        # Print county results
        county_results =(
            f"{county_name}: {vote_percentage:.1f}% ({votes:,})\n")
        print(county_results)
        
    
        
        # Determine winning county and its vote count        
        if (votes > turnout_votes) and (vote_percentage > turnout_percentage):
            turnout_votes = votes
            largest_turnout_county = county_name
            turnout_percentage = vote_percentage
    
        # Print county with largest turnout
        largest_county = (f"\n----------------------\n"
            f"Largest County Turnout: {largest_turnout_county}\n"
            f"--------------------\n")
        print(largest_county)
    
 
    
    # Save final candidate vote count to text file
    for candidate_name in candidate_votes:
        
        # Retrieve vot count and percentage
        votes = candidate_votes.get(candidate_name)
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        
        # Print vote count and %or votes for the candidates
        print(candidate_results)
    
       
        
        # Determine winning vote count, winning % (and candidate)
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage
            
            
        # Print winning candidate
        winning_candidate_summary = (
            f"-----------------------\n"
            f"Winning Vote Count:  {winning_count:,}\n"
            f"Winning Percentage: {winning_percentage:.1f}%\n"
            f"-----------------------\n")
        print(winning_candidate_summary)






    
        # Save to text file
        #txt_file.write(winning_candidate_summary)
         # Save to text file
        #txt_file.write(candidate_results)
        # Save to text file
        # txt_file.write(largest_county)
            # Save to text file
        #txt_file.write(county_results)
        
    # Save the results to text file
    #lines = ['election_results', 'The results of the election are as follows:']
    #with open ('election_results.txt', 'w') as f:
     #   for line in lines:
      #      f.write(line)
       #     f.write('\n')
       
       # Assign file to save
    #file_to_save  = os.path.join("..", "analysis", "election_results.txt")


            
            