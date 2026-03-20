import pandas as pd

# Load the data
df = pd.read_csv('superstore.csv', encoding='latin-1')

# Transform 1 — Fix date columns
df['Order Date'] = pd.to_datetime(df['Order Date'], format='%d-%m-%Y')
df['Ship Date'] = pd.to_datetime(df['Ship Date'], format='%d-%m-%Y')

# Transform 2 — Add new columns
df['Order Year'] = df['Order Date'].dt.year
df['Order Month'] = df['Order Date'].dt.month
df['Delivery Days'] = (df['Ship Date'] - df['Order Date']).dt.days

# Transform 3 — Round Sales and Profit
df['Sales'] = df['Sales'].round(2)
df['Profit'] = df['Profit'].round(2)

# Check the result
print("Shape:", df.shape)
print("\nNew columns added:")
print(df[['Order Date', 'Order Year', 'Order Month', 'Delivery Days']].head())

# Save cleaned data
df.to_csv('superstore_cleaned.csv', index=False)
print("\nCleaned data saved!")
