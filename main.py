# Election Analysis
# Reads election data from a CSV file, tallies votes by candidate and county,
# calculates percentages, determines the winner, and outputs results to the
# terminal and a text file.

import os
import csv

# ---------------------------------------------------------------------------
# File paths
# ---------------------------------------------------------------------------
election_data_csv = os.path.join("data", "election_data.csv")
analysis_output   = os.path.join("analysis", "election_analysis.txt")

# ---------------------------------------------------------------------------
# Tracking variables
# ---------------------------------------------------------------------------
total_votes = 0

# Candidate metrics  {candidate_name: vote_count}
candidate_votes = {}
candidate_list  = []

# County metrics  {county_name: vote_count}
county_votes = {}
county_list  = []

# Winner / largest county trackers
winning_candidate       = ""
winning_count           = 0
winning_percentage      = 0.0

largest_county_turnout  = ""
largest_county_count    = 0

# ---------------------------------------------------------------------------
# Read the CSV and tally votes
# ---------------------------------------------------------------------------
with open(election_data_csv, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Skip the header row
    header = next(csvreader)

    for row in csvreader:
        # Unpack columns
        ballot_id  = row[0]
        county     = row[1]
        candidate  = row[2]

        # Total vote counter
        total_votes += 1

        # --- Candidate tracking ---
        if candidate not in candidate_votes:
            candidate_votes[candidate] = 0
            candidate_list.append(candidate)
        candidate_votes[candidate] += 1

        # --- County tracking ---
        if county not in county_votes:
            county_votes[county] = 0
            county_list.append(county)
        county_votes[county] += 1

# ---------------------------------------------------------------------------
# Build the results report
# ---------------------------------------------------------------------------
results = (
    "\nElection Results\n"
    "=========================\n"
    f"Total Votes: {total_votes:,}\n"
    "=========================\n"
    "\n"
    "County Votes:\n"
    "-------------------------\n"
)

# County breakdown
for county in county_list:
    c_votes = county_votes[county]
    c_percentage = (c_votes / total_votes) * 100

    results += f"  {county}: {c_percentage:.1f}% ({c_votes:,})\n"

    # Track largest county turnout
    if c_votes > largest_county_count:
        largest_county_count   = c_votes
        largest_county_turnout = county

results += (
    "-------------------------\n"
    f"Largest County Turnout: {largest_county_turnout}\n"
    "-------------------------\n"
    "\n"
    "Candidate Votes:\n"
    "-------------------------\n"
)

# Candidate breakdown
for candidate in candidate_list:
    v = candidate_votes[candidate]
    v_percentage = (v / total_votes) * 100

    results += f"  {candidate}: {v_percentage:.3f}% ({v:,})\n"

    # Track the winner
    if v > winning_count:
        winning_count      = v
        winning_candidate  = candidate
        winning_percentage = v_percentage

results += (
    "-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.3f}%\n"
    "=========================\n"
)

# ---------------------------------------------------------------------------
# Print to terminal
# ---------------------------------------------------------------------------
print(results)

# ---------------------------------------------------------------------------
# Export to text file
# ---------------------------------------------------------------------------
# Ensure the output directory exists
os.makedirs(os.path.dirname(analysis_output), exist_ok=True)

with open(analysis_output, "w") as txt_file:
    txt_file.write(results)

print(f"Results saved to {analysis_output}")
