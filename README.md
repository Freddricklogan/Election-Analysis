# Election Analysis

## Overview
This project automates the analysis of election results using Python. Given a
CSV file of individual ballots, the script tallies total votes, breaks down
results by county and by candidate, calculates vote percentages, identifies the
county with the largest voter turnout, and determines the winning candidate.

## Repository Structure

```
Election-Analysis/
├── main.py                        # Main analysis script
├── data/
│   └── election_data.csv          # Source election data (Ballot ID, County, Candidate)
├── analysis/
│   └── election_analysis.txt      # Generated results (created when the script runs)
├── .gitignore
└── README.md
```

## Data Format
The input CSV (`data/election_data.csv`) must contain three columns:

| Column      | Description                          |
|-------------|--------------------------------------|
| Ballot ID   | Unique identifier for each ballot    |
| County      | County where the ballot was cast     |
| Candidate   | Name of the candidate voted for      |

## How to Run

1. Make sure Python 3.6+ is installed.
2. Clone this repository and navigate into it:
   ```bash
   git clone <repo-url>
   cd Election-Analysis
   ```
3. Run the script:
   ```bash
   python3 main.py
   ```
4. Results will print to the terminal and be saved to `analysis/election_analysis.txt`.

## Analysis Performed
The script calculates and reports:

- **Total votes** cast across all counties
- **County breakdown** -- vote count and percentage of total votes for each county
- **Largest county turnout** -- the county with the most votes
- **Candidate breakdown** -- vote count and percentage for each candidate
- **Election winner** -- the candidate with the most votes, along with their vote count and winning percentage

## Sample Output

```
Election Results
=========================
Total Votes: 100
=========================

County Votes:
-------------------------
  Jefferson: 27.0% (27)
  Denver: 49.0% (49)
  Arapahoe: 24.0% (24)
-------------------------
Largest County Turnout: Denver
-------------------------

Candidate Votes:
-------------------------
  Charles Casper Stockham: 20.000% (20)
  Diana DeGette: 69.000% (69)
  Raymon Anthony Doane: 11.000% (11)
-------------------------
Winner: Diana DeGette
Winning Vote Count: 69
Winning Percentage: 69.000%
=========================
```

## Technologies
- Python 3
- `csv` module (standard library)
- `os` module (standard library)
