# Bygg en ETL-process
# Läs in data från två olika CSV-filer:
# a. sales_2025.csv: Försäljningsdata.
# b. customers.csv: Kundinformation.
# Hantera saknade värden och skapa en ny kolumn Total_Sales.
# Kombinera data baserat på en gemensam kolumn (CustomerID).
# Spara den transformerade datan i en ny CSV-fil.


#för att hantera filer
import pandas as pd


# Läs in försäljningsdata och kunddata
# väljer namn som ska stå för filerna jag vill slå ihop
sales_data = pd.read_csv("/Users/viktorheidmark/Documents/DMSTO24-DS/DS9/ovningar/sales_2025.csv")
customer_data = pd.read_csv("/Users/viktorheidmark/Documents/DMSTO24-DS/DS9/ovningar/customers.csv")

# rad 20 lägga till en ny kolumn som heter total sales och multiplicera price och quantity
# rad 21 välj tillfälligt namn på filen som ska skapas
# rad 21 pd.merge för att slå ihop 2 filer sales_data och customer_data baserat på CustomerID
# rad 21 för att customerID är gemesam (on="CustomerID")
# rad 21 använd how="inner" för att bara ta med de rader som finns i båda filerna
sales_data["Total_Sales"] = sales_data["Price"] * sales_data["Quantity"]
processed_data = pd.merge(sales_data, customer_data, on="CustomerID", how="inner")

# rad 29 ladda ner filen till en ny fil som heter final_data.csv 
# rad 29 och använd index=False för att inte spara index
processed_data.to_csv("final_data.csv", index=False)
print("ETL-processen är klar!")