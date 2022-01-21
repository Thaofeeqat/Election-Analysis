import csv
import os

file_to_load = os.path.join("Election_Analysis", "Resources", "election_results.csv")
with open(file_to_load) as election_data:
    print(election_data)

file_to_save = os.path.join("Election_Analysis", "analysis", "election_analysis.txt")
open(file_to_save, "w")

file_to_save = os.path.join("Election_Analysis", "analysis", "election_analysis.txt")

outfile = open(file_to_save, "w")
outfile.write("Hello World")

file_to_save = os.path.join("Election_Analysis", "analysis", "election_analysis.txt" )

with open(file_to_save, "w") as txt_file:
    txt_file.write("Arapahoe")

file_to_save = os.path.join("Election_Analysis", "analysis 1", "election_analysis.txt")
open(file_to_save, "w")

file_to_save = os.path.join("Election_Analysis", "analysis 1", "election_analysis.txt")

outfile = open(file_to_save, "w")
outfile.write("Arapahoe")

file_to_save = os.path.join("Election_Analysis", "analysis 1", "election_analysis.txt")
with open(file_to_save, "w") as txt_file:
    txt_file.write("Arapahoe\nDenver\nJefferson")


# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Election_analysis", "Resources", "election_results.csv")

# Assign a variable to save the file to a path.
file_to_save = os.path.join("Election_Analysis", "Resources", "election_results.txt") 

# Open the election result and read the file.
with open (file_to_load) as election_data:
    print(election_data)
file_reader = csv.reader(election_data)
for row in file_reader:
    print(row)
print(election_data)