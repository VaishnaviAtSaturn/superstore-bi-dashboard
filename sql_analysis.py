import pandas as pd
import sqlite3

df = pd.read_csv("superstore_cleaned.csv")


conn = sqlite3.connect("superstore.db")
df.to_sql("sales", conn, if_exists="replace", index=False)

print("Database created successfully!")
print("-" * 50)


q1 = """
SELECT Region, 
       ROUND(SUM(Sales), 2) as Total_Sales,
       ROUND(SUM(Profit), 2) as Total_Profit
FROM sales
GROUP BY Region
ORDER BY Total_Sales DESC
"""
print("Q1: Revenue & Profit by Region")
print(pd.read_sql(q1, conn))
print()


q2 = """
SELECT Category,
       ROUND(SUM(Sales), 2) as Total_Sales,
       ROUND(SUM(Profit), 2) as Total_Profit,
       ROUND(SUM(Profit) * 100.0 / SUM(Sales), 2) as Profit_Margin_Pct
FROM sales
GROUP BY Category
ORDER BY Profit_Margin_Pct DESC
"""
print("Q2: Profit Margin by Category")
print(pd.read_sql(q2, conn))
print()


q3 = """
SELECT [Sub-Category],
       ROUND(SUM(Profit), 2) as Total_Profit
FROM sales
GROUP BY [Sub-Category]
ORDER BY Total_Profit ASC
LIMIT 5
"""
print("Q3: Top 5 Loss-Making Sub-Categories")
print(pd.read_sql(q3, conn))
print()


q4 = """
SELECT 
    CASE 
        WHEN Discount = 0 THEN 'No Discount'
        WHEN Discount <= 0.2 THEN 'Low (0-20%)'
        WHEN Discount <= 0.4 THEN 'Medium (20-40%)'
        ELSE 'High (40%+)'
    END as Discount_Band,
    COUNT(*) as Orders,
    ROUND(AVG(Profit), 2) as Avg_Profit
FROM sales
GROUP BY Discount_Band
ORDER BY Avg_Profit DESC
"""
print("Q4: Impact of Discount on Profit")
print(pd.read_sql(q4, conn))
print()


q5 = """
SELECT Year,
       ROUND(SUM(Sales), 2) as Total_Sales,
       COUNT(DISTINCT [Order ID]) as Total_Orders
FROM sales
GROUP BY Year
ORDER BY Year
"""
print("Q5: Year-over-Year Sales Growth")
print(pd.read_sql(q5, conn))
print()

conn.close()
print("Done! superstore.db file saved.")