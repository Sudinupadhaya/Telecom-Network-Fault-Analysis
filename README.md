# Telecom Network Fault Analysis

A small telecom data analysis project using Python. The project looks at network fault records and summarizes which regions, technologies, sites, and fault types need more attention.

## What this project does

- Reads telecom fault data from a CSV file
- Checks total incidents, average downtime, and repeated site issues
- Compares faults by region and technology
- Finds common fault types
- Reviews severity distribution
- Saves summary charts inside the project folder

## Files

```text
README.md
main.py
requirements.txt
telecom_fault_data.csv
telecom_fault_analysis.py
```

## Dataset columns

```text
fault_id, date, region, site_id, technology, fault_type,
severity, downtime_minutes, affected_users, resolution_status
```

## How to run

Install the required libraries:

```bash
pip install -r requirements.txt
```

Run the project:

```bash
python main.py
```

The script prints a short summary in the terminal and creates charts in the `results` folder.

## Notes

The dataset included here is a sample dataset created for practice. The same analysis structure can be used with real NOC or telecom operation data after replacing the CSV file.

## Author

Sudin Upadhaya
