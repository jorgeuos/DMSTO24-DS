"""
Läs in data från två olika CSV-filer:
sales_2025.csv: Försäljningsdata.
customers.csv: Kundinformation.
1. Hantera saknade värden och skapa en ny kolumn Total_Sales.
2. Kombinera data baserat på en gemensam kolumn (CustomerID).
3. Spara den transformerade datan i en ny CSV-fil.
"""
import pandas as pd

sales_data = pd.read_csv("sales_2025.csv")
customer_data = pd.read_csv("customers.csv")

merged_data = pd.merge(sales_data, customer_data, on="CustomerID", how="inner")

merged_data["Total_Sales"] = merged_data["Price"] * merged_data["Quantity"]

print(merged_data)

merged_data.to_csv("combined_data.csv")
