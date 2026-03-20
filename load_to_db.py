import pandas as pd
from sqlalchemy import create_engine

# Load cleaned data
df = pd.read_csv('superstore_cleaned.csv')

# Connect to PostgreSQL
engine = create_engine('postgresql://postgres:akarsh18@localhost:5432/etl_project')

# Load data into PostgreSQL
df.to_sql('sales', engine, if_exists='replace', index=False)

print("Data loaded successfully!")
print("Total rows loaded:", len(df))
