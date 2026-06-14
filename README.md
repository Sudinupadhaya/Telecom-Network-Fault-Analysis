# Telecom Network Fault Analysis

This is a small Python project for analyzing telecom network fault records. I made it to practice working with operational telecom data and to summarize common issues such as repeated site faults, downtime, affected users, and fault patterns by region and technology.

## What this project does

- Reads telecom fault records from a CSV file
- Shows total faults and average downtime
- Finds sites with repeated faults
- Compares fault counts by region
- Compares fault counts by network technology
- Checks the most common fault types
- Calculates average downtime by region
- Creates simple charts inside the `results` folder

## Files

```text
README.md
main.py
requirements.txt
telecom_fault_data.csv
telecom_fault_analysis.py
results/
```

## Dataset columns

```text
fault_id
date
region
site_id
technology
fault_type
severity
downtime_minutes
affected_users
resolution_status
```

## Tools used

- Python
- Pandas
- Matplotlib

## How to run

Install the required libraries:

```bash
pip install -r requirements.txt
```

Run the project:

```bash
python main.py
```

After running, the script prints a short summary in the terminal and saves charts in the `results` folder.

## Output charts

The project creates charts such as:

- Fault count by region
- Fault count by technology
- Most common fault types
- Average downtime by region

## Notes

The dataset included in this repository is a sample dataset created for practice. The same analysis can be used with real NOC or telecom operations data by replacing the CSV file.

## Author

Sudin Upadhaya
