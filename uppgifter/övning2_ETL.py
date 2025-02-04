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

# rad 21 lägga till en ny kolumn som heter total sales och multiplicera price och quantity
sales_data["Total_Sales"] = sales_data["Price"] * sales_data["Quantity"]

# rad 27 välj tillfälligt namn på filen som ska skapas
# rad 27 pd.merge för att slå ihop 2 filer sales_data och customer_data baserat på CustomerID
# rad 27 för att customerID är gemesam (on="CustomerID")
# rad 27 använd how="inner" för att bara ta med de rader som finns i båda filerna
combined_data = pd.merge(sales_data, customer_data, on="CustomerID", how="inner")



# rad 32 döp nya filen tillfälligt för att skapa funktion och Filtrera rader där Region är "North".
north_sales = combined_data[combined_data["Region"] == "North"]

# rad 36 ladda ner filen till en ny fil som heter final_data.csv 
# rad 36 och använd index=False för att inte spara index
north_sales.to_csv("north_sales.csv", index=False)
print("Pipeline färdig! Data sparad i 'north_sales.csv'")

