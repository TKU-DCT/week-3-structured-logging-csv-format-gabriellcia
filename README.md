[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/_yF6dieQ)
# Week 3 – Structured Logging (CSV Format)

## Objective

Modify your logging system to save data into a CSV file format with the following columns:

- Timestamp
- CPU usage
- Memory usage
- Disk usage

Use Python's built-in `csv` module to write data.

## Tasks

- Create `log.csv` if it doesn't exist
- Add a header row: `Timestamp, CPU, Memory, Disk`
- Append one row each time the script is run

## Example Output (log.csv)

Timestamp,CPU,Memory,Disk
2025-09-21 14:10:45,17.4,43.1,58.3
2025-09-21 14:12:01,12.8,40.5,58.2

## Submission

- Push `main.py` to GitHub
- Push `log.csv` with at least 2 records
- Include a screenshot of execution or log file view
