# Bonusuppgift
# Gruppera data baserat på Region och summera Total_Sales.
# Skapa ett stapeldiagram som visar total försäljning per region.

import pandas as pd

sales_data = pd.read_csv("/Users/viktorheidmark/Documents/DMSTO24-DS/DS9/ovningar/sales_2025.csv")
customer_data = pd.read_csv("/Users/viktorheidmark/Documents/DMSTO24-DS/DS9/ovningar/customers.csv")

sales_data["Total_sales"] = sales_data["price"] * sales_data["quantity"]
combined_data = pd.merge(sales_data, customer_data, on="CustomerID", how="inner")


# Gruppera data och summera försäljning
region_sales = combined_data.groupby("Region")["Total_Sales"].sum()
print(region_sales)