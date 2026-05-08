# ism2411-data-cleaning-copilot
## Overview

This project is a simple data cleaning pipeline built in Python using pandas. The goal is to take a messy sales dataset, Fix it, and output a structured version that is easier to analyze. The project also demonstrates how GitHub Copilot can be used as a coding assistant during development.

## What This Project Does

The script performs the following cleaning steps:

- Loads a raw CSV file containing messy sales data  
- Standardizes column names (lowercase, underscores, no extra spaces)  
- Cleans text fields like product names and categories  
- Handles missing values in price and quantity columns  
- Removes invalid rows such as negative prices or quantities  
- Saves the cleaned dataset into a new CSV file
## How to Run the Code

Make sure you have Python installed, then install pandas if needed:
Run the script from the project root folder:
```bash
pip install pandas
Run the script from the project root folder:
python src/data_cleaning.py
After running, the cleaned dataset will be saved here:
data/processed/sales_data_clean.csv
