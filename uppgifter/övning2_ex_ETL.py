# Extract:
# Läs in sales_2025.csv och customers.csv.
# Transform:
# Hantera saknade värden i Price och Quantity.
# Skapa kolumnen Total_Sales (Price * Quantity).
# Filtrera rader där Region är "North".
# Load:
# Spara den transformerade datan i en ny CSV-fil (north_sales.csv).


#för att hantera filer
import pandas as pd


# Läs in försäljningsdata och kunddata
# väljer namn som ska stå för filerna jag vill slå ihop
sales_data = pd.read_csv("/Users/viktorheidmark/Documents/DMSTO24-DS/DS9/ovningar/sales_2025.csv")
customer_data = pd.read_csv("/Users/viktorheidmark/Documents/DMSTO24-DS/DS9/ovningar/customers.csv")

# Transform
sales_data["Price"].fillna(sales_data["Price"].mean(), inplace=True)
sales_data["Quantity"].fillna(0, inplace=True)
sales_data["Total_Sales"] = sales_data["Price"] * sales_data["Quantity"]

# Kombinera data och filtrera
combined_data = pd.merge(sales_data, customer_data, on="CustomerID", how="inner")
north_sales = combined_data[combined_data["Region"] == "North"]


#testa den nya datan innan vi sparar den
print(north_sales.head())

# Load
north_sales.to_csv("north_sales.csv", index=False)
print("Pipeline färdig! Data sparad i 'north_sales.csv'")