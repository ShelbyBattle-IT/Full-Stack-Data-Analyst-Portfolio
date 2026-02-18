"""
Footwear Sales Analysis
Author: Shelby Battle
Purpose: Analyze footwear sales data using Python to automate insights
"""

from pathlib import Path
import pandas as pd


def main():
    # Set file path relative to project root
    base_dir = Path(__file__).resolve().parents[1]
    file_path = base_dir / "02_excel_storytelling" / "Footwear_Sales_Performance_Dashboard_Final.xlsx"

    # Load cleaned data sheet
    df = pd.read_excel(file_path, sheet_name="02_CLEAN_DATA")

    print("\n--- Data Preview ---")
    print(df.head())

    print("\n--- Data Info ---")
    print(df.info())

    # Key Metrics
    total_revenue = df["Revenue"].sum()
    revenue_by_region = df.groupby("Region")["Revenue"].sum()
    revenue_by_channel = df.groupby("Channel")["Revenue"].sum()

    print("\n--- Key Metrics ---")
    print(f"Total Revenue: {total_revenue}")

    print("\nRevenue by Region:")
    print(revenue_by_region)

    print("\nRevenue by Channel:")
    print(revenue_by_channel)


if __name__ == "__main__":
    main()
