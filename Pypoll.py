import csv
from email import header
import os


file_to_load = os.path.join('Election_Analysis/Resources/election_results.csv') 
with open(file_to_load) as election_data:
    print(election_data)

election_data = open(file_to_load, 'r')

file_to_save = os.path.join("Election_Analysis", "analysis", "election_analysis.txt" )
open(file_to_save, "w")

file_to_save = os.path.join("Election_Analysis", "analysis", "election_analysis.txt" )

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

file_reader = csv.reader(election_data)

for row in file_reader:
    print(row)

# Print the header row
headers = next(file_reader)
print(headers)
