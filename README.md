# Telecom Network Fault Analysis

A Python project for analyzing telecom network fault records. It summarizes fault patterns by region, technology, site, downtime, affected users, and fault type.

I built this project to practice telecom operations data analysis using a simple CSV dataset and Python.

## Overview

Network operation teams need to know where faults happen most often, which sites repeat issues, and which fault types cause more downtime. This project gives a basic view of those patterns using Pandas and Matplotlib.

## Main Analysis

- Total number of network faults
- Average downtime in minutes
- Total affected users
- Top repeated fault sites
- Fault count by region
- Fault count by technology
- Most common fault types
- Average downtime by region

## Tools Used

- Python
- Pandas
- Matplotlib

## Files

```text
main.py
telecom_fault_analysis.py
telecom_fault_data.csv
requirements.txt
README.md
results/
```

## Dataset Columns

```text
fault_id, date, region, site_id, technology, fault_type,
severity, downtime_minutes, affected_users, resolution_status
```

## How to Run

Install the required libraries:

```bash
pip install -r requirements.txt
```

Run the analysis:

```bash
python main.py
```

After running the project, charts are saved in the `results` folder.

## Output Charts

- `faults_by_region.png`
- `faults_by_technology.png`
- `fault_types.png`
- `average_downtime_by_region.png`

## Notes

The dataset in this repository is a sample dataset for practice. The same structure can be used with real NOC or telecom operations data by replacing the CSV file.

## Author

Sudin Upadhaya
