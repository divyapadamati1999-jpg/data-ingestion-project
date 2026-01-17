 # Data Ingestion Pipeline – Olist E-commerce Dataset

## Overview
This project demonstrates a step-by-step data ingestion pipeline using
real-world e-commerce data. The pipeline focuses on loading raw data,
validating data quality, joining related tables, and producing a clean,
enriched dataset ready for downstream ingestion.

All transformations are implemented and traced using Jupyter Notebook.

## Dataset
Source: Olist Brazilian E-commerce Public Dataset

Tables used:
- Orders
- Customers
- Order Items
- Products

## Pipeline Steps
1. Load raw CSV datasets
2. Validate row counts, duplicates, and missing values
3. Convert timestamp and numeric columns
4. Join related tables using appropriate join strategies
5. Trace and explain missing values after each join

## Step 4: Join Related Tables
The datasets were joined incrementally based on their relationships and
level of detail (grain):

- Orders → Customers (one-to-one, left join)
- Orders → Order Items (one-to-many, left join)
- Order Items → Products (many-to-one, left join)

Row counts and missing values were checked after each join to ensure no
orders were lost and that missing values aligned with real business scenarios
such as cancelled or unavailable orders.

## Tools Used
- Python
- Pandas
- Jupyter Notebook
- Git & GitHub

## Notes
Raw and processed data files are excluded from GitHub using `.gitignore`.

