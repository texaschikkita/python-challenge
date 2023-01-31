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

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # Read and analyze the data here.
    reader = csv.reader(election_data)

    # Read the header row.
    header= next(reader)   #not headers

    # Print each row in the CSV file.
    for row in reader:
        
        # Run leader animation
        print(".  ", end=""),
        
        # Add to the total vote count.   total_votes = total_votes + 1 (long format)   Use shorter format to write the same line
        total_votes += 1 
        
        # Note select lines then hit ctrl+'/?' for shortcut to comment out section 
    
        # Get the candidate name from each row.
        candidate_name = row[2]

        # If the candidate does not match any existing candidate... 
        if candidate_name not in candidate_options:
            
            # ...add name to candidate list.  Then:
            candidate_options.append(candidate_name)

            # Begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0
        
        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1
        
# Create output report
with open(file_to_output, "w") as txt_file:

    # Print final vote count to terminal
    election_results = (
        f"\n\nElection Results\n"
        f"__________________________\n"
        f"Total Votes:  {total_votes}\n"
        f"__________________________\n"
        )
    print(election_results, end="")
    
    # Print to output file
    txt_file.write(election_results)

    # Loop through counts to determine winner 
    for candidate in candidate_votes:
        
        # Retrieve vote count and percentage (use float not integer)
        votes = candidate_votes.get(candidate)                                                         
        vote_percentage =float(votes) / float(total_votes) * 100                              
        
        # Determine winning vote count and candidate
        if  (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate                                                               
        
        # Print the candidate name and percentage of votes. print (f"[{candidate}]: received {votes} votes, receiving {vote_percentage:.f}% of the vote")"
        voter_output = f"{candidate}: {vote_percentage:.3f}% ({votes})\n"
        print(voter_output,  end="")   
        
        # Save candidate's voter count to text file
        txt_file.write(voter_output)
        
        
# Print the winning candidate results
winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"                                              # 3f or 1f test and see;  should be 1 bc just for winner here
        f"-------------------------\n")
print(winning_candidate_summary) 

# Print the winning candidate results to text file
with open(file_to_output, "w") as txt_file:                               
    txt_file.write(winning_candidate_summary)
    txt_file.write(election_results)



      

