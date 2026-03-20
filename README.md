# Sales ETL Pipeline + Power BI Dashboard

## Overview
An end-to-end ETL pipeline that extracts raw sales data, 
transforms it using Python, loads it into PostgreSQL and 
visualizes it in an interactive Power BI dashboard.

## Tools Used
- Python
- Pandas
- PostgreSQL
- SQLAlchemy
- Power BI

## ETL Process
- Extract: Loaded raw CSV data using Pandas
- Transform: Fixed date formats, added new columns 
  (Order Year, Order Month, Delivery Days)
- Load: Pushed cleaned data into PostgreSQL database

## Dashboard Features
- Total Sales, Profit and Orders summary cards
- Sales by Region (Bar Chart)
- Monthly Sales Trend (Line Chart)
- Profit by Category (Pie Chart)
- Top 5 Products by Sales (Column Chart)

## Key Insights
- West region has highest sales ($725K)
- Technology is most profitable category ($145K)
- Average delivery time calculated per order
- Texas has highest losses across all states
