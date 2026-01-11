# -*- coding: utf-8 -*-
"""
Created on Sat Jan  3 20:04:41 2026

@author: padam
"""

import pandas as pd
#####orders table exploration##
#load data#
orders=pd.read_csv(r"C:\data_sparta\data_ingestion\Data\raw\olist_orders_dataset.csv")
#preview of data#
print(orders.head())
#shape of the table#
print("\nShape of orders table (rows, columns):")
print(orders.shape)
#Column names
print("\nColumn names:")
print(orders.columns)
#data types
print("\nData types:")
print(orders.dtypes)
#missing values
print("\nMissing values per column:")
print(orders.isnull().sum())
#uniqueness 
print("\nUnique order_id count:")
print(orders['order_id'].nunique())
# order status categories
orders['order_status'].unique()
#order columns
print(orders.columns)


########## Order_items table exploration###
import pandas as pd
order_items=pd.read_csv(r"C:\data_sparta\data_ingestion\Data\raw\olist_order_items_dataset.csv")
print(order_items.head())
print(order_items.shape)
print(order_items.columns)
print(order_items.dtypes)
print(order_items.isnull().sum())
print(order_items['order_id'].nunique())
print(order_items['order_item_id'].nunique())
print(len(order_items))
print("\nUnique product_id count:")
print(order_items['product_id'].nunique())

######product table exploration###
import pandas as pd
products=pd.read_csv(r"C:\data_sparta\data_ingestion\Data\raw\olist_products_dataset.csv")
print(products.head())
print(products.shape)
print(products.columns)
print(products.dtypes)
print(products.isnull().sum())
print("\nUnique product_id count:")
print(products['product_id'].nunique())

######3 customers ##
import pandas as pd
customers=pd.read_csv(r"C:\data_sparta\data_ingestion\Data\raw\olist_customers_dataset.csv")
print(customers.head())
print(customers.shape)
print(customers.columns)
print(customers.dtypes)
print(customers.isnull().sum())
print("\nTotal rows in customers table:", len(customers))
print("Unique customer_id count:", customers['customer_id'].nunique())
print("\nUnique customer_unique_id count:")
print(customers['customer_unique_id'].nunique())





