# SQL + Python Sales Analysis

## Project Overview
This project extends the Excel footwear sales analysis into Python using pandas.  
The script loads cleaned sales data and calculates business metrics programmatically.

---

## Tools Used
- Python 3
- pandas
- openpyxl
- Excel (data source)

---

## Key Metrics Calculated

- Total Revenue: $3,260
- Revenue by Region:
  - West: 1,110
  - East: 880
  - Midwest: 685
  - South: 585
- Revenue by Channel:
  - Direct-to-Consumer (DTC): 2,125
  - Retail: 1,135

---

## What This Demonstrates

- Reading Excel files with pandas
- Selecting specific sheets
- Data inspection using `.head()` and `.info()`
- Groupby aggregation
- Business KPI calculation
- Automating reporting logic

---

## How to Run

From the project root:

```bash
cd 03_SQL_Python_Practice
python3 footwear_sales_analysis.py

