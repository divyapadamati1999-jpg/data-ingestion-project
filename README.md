# Data Ingestion Project – Olist E-commerce Dataset

## Project Overview
This project focuses on sourcing, cleaning, validating, and joining data from a real-world e-commerce dataset (Olist).
The goal is to prepare high-quality, analysis-ready data following best practices in data ingestion.

## Dataset
This project uses the following relational CSV files:
- olist_orders_dataset.csv
- olist_customers_dataset.csv
- olist_order_items_dataset.csv
- olist_products_dataset.csv

## Folder Structure


## Cleaning Steps Completed
- Converted timestamp columns to datetime (orders + order_items)
- Validated primary keys and checked duplicates (order_id, customer_id, product_id)
- Preserved event-based missing timestamps (e.g., cancelled/unavailable orders)
- Converted numeric fields (price, freight_value, dimensions) to numeric types
- Documented missing product metadata (category/description fields)

## Joining Logic Completed
- customers → orders (join on customer_id, many-to-one)
- orders → order_items (join on order_id, one-to-many)
- order_items → products (join on product_id, many-to-one)
- Used left joins to preserve transactional integrity

## Output Files
Saved to: `data/processed/`
- customers_clean.csv
- orders_clean.csv
- order_items_clean.csv
- products_clean.csv
- olist_joined.csv (final joined dataset)

## Next Steps
- Add data validation rules (null thresholds, allowed order_status values, referential checks)
- Add logging and error handling
- Explore automation and AWS ingestion (S3/Athena)
