# SQL and Python Practice

This section showcases my ability to work directly with data at scale and automate analytical workflows.

## SQL Analysis: Footwear Sales Performance (PostgreSQL)

This analysis answers key business questions using PostgreSQL and transactional sales data.

### Revenue by Product Category
```sql
SELECT
  product_category,
  SUM(revenue) AS total_revenue
FROM footwear_sales
GROUP BY product_category
ORDER BY total_revenue DESC;

Insight:
Running is the top revenue-driving category, outperforming Training and Lifestyle, indicating strong demand for performance footwear.



---
### Revenue by Region
```markdown
### Revenue by Region
```sql
SELECT
  region,
  SUM(revenue) AS total_revenue
FROM footwear_sales
GROUP BY region
ORDER BY total_revenue DESC;

Insight:
The West region leads revenue, while the Midwest and South underperform, suggesting opportunities for targeted regional strategies.



---
### DTC vs Retail Performance
```markdown
### DTC vs Retail Performance
```sql
SELECT
  channel,
  SUM(revenue) AS total_revenue,
  SUM(units_sold) AS total_units
FROM footwear_sales
GROUP BY channel
ORDER BY total_revenue DESC;

Insight:
Direct-to-Consumer significantly outperforms Retail in both revenue and units sold, highlighting the strength of owned channels.



---
### Monthly Revenue Trend
```markdown
### Monthly Revenue Trend
```sql
SELECT
  year,
  month,
  SUM(revenue) AS monthly_revenue
FROM footwear_sales
GROUP BY year, month
ORDER BY year, month;

Insight:
Revenue peaks in January with a secondary increase in October, reflecting seasonal purchasing behavior.



---
### Quarterly Revenue Trend
```markdown
### Quarterly Revenue Trend
```sql
SELECT
  quarter,
  SUM(revenue) AS total_revenue
FROM footwear_sales
GROUP BY quarter
ORDER BY total_revenue DESC;

Insight:
Q1 shows the strongest performance, while Q2 is the weakest, indicating mid-year growth opportunities.



---
SQL skills demonstrated:
- Joins (inner, left, multi-table)
- Common Table Expressions (CTEs)
- Window functions (ranking, rolling metrics)
- Subqueries for advanced filtering and aggregation

Python skills demonstrated:
- Data cleaning and validation with pandas
- Automation scripts for recurring tasks
- Logic to support alerts and data refreshes

What this section proves:
- I don’t rely on manual processes
- I can build repeatable, scalable analysis
- I design systems that make analysis easier over time
