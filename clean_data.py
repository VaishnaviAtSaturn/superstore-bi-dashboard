import pandas as pd


df = pd.read_csv("Sample - Superstore.csv", encoding='latin-1')
print(df.head())
print(df.columns)

print(df.isnull().sum())  


df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Ship Date'] = pd.to_datetime(df['Ship Date'])

df['Year'] = df['Order Date'].dt.year
df['Month'] = df['Order Date'].dt.month


df['Profit Margin %'] = (df['Profit'] / df['Sales'] * 100).round(2)


df.to_csv("superstore_cleaned.csv",index=False)
