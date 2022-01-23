import csv
import os

file_to_load = os.path.join('Election_Analysis/Resources/election_results.csv') 

file_to_save = os.path.join("Election_Analysis", "analysis 1", "election_analysis.txt" )

total_votes = 0

candidate_options = []
candidate_votes = {}

winning_candidate = ""
winning_count = 0
winning_percentage = 0
election_data = open(file_to_load, 'r')
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
# Print the header row
    headers = next(file_reader)

    for row in file_reader:
        print(row)
# Add to the total vote count.
    total_votes += 1
    print(total_votes)   
    candidate_name = row[2]

# If the candidates does not match any existing candidate...
    if candidate_name not in candidate_options:
    #Add it to the list of candidates.
        candidate_options.append(candidate_name)
        candidate_votes[candidate_name] = 0
    candidate_votes[candidate_name] += 1
with open(file_to_save, "w") as txt_file:
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    txt_file = open(file_to_save, "w")
    # Save the final vote count to the text file.
    txt_file.write(election_results)

    for candidate_name in candidate_votes:
        votes = candidate_votes[candidate_name]
        votes_percentage = float(votes) / float(total_votes) * 100
        print(f"{candidate_name}: {votes_percentage:.1f}% ({votes:,})\n")

        if (votes > winning_count) and (votes_percentage > winning_percentage):
            winning_count = votes
        winning_percentage = votes_percentage
    print(f"{winning_candidate}: {winning_count:.1f}% ({votes:,})\n")

    #print(f"{candidate_name}: {votes_percentage:.1f}% ({votes:,})\n")

    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")

    #print(winning_candidate_summary)

candidate_results = (f"{candidate_name}: {votes_percentage:.1f}% ({votes:,})\n")
print(candidate_results)
txt_file.write(candidate_results)
