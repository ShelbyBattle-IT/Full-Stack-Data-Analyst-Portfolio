"""
Footwear Sales Analysis
Author: Shelby Battle
Purpose: Analyze footwear sales data using Python to automate insights
"""

import pandas as pd

# Load cleaned sales data
df = pd.read_csv("../02_excel_storytelling/footwear_clean_data.csv")

# Preview data
print(df.head())
print(df.info())
