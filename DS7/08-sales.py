import pandas as pd
"""
Läs in data från sales.csv.
Skapa en ny kolumn Total Sales (Price * Quantity).
Filtrera ut försäljning där Total Sales > 500.
Summera total försäljning per produkt.
Spara två filer:
En ny CSV-fil med filtrerad data.
En Excel-fil med den aggregerade försäljningen.
"""

# Läs in en csv
df = pd.read_csv("sales.csv")

# Skapa kolumnen Total Sales
df["Total Sales"] = df["Price"] * df["Quantity"]

# Filtrera ut försäljning där Total Sales > 500.
filtered_data = df[df["Total Sales"] >= 500]
print(filtered_data)

print("Total försäljning:")
print(df["Total Sales"].sum())

# En ny CSV-fil med filtrerad data.
filtered_data.to_csv("filtered_data.csv")

print(df)

# Summera total försäljning per produkt.
print("Summera total försäljning per produkt.")
grouped = df.groupby("Product")["Total Sales"].sum()
print(grouped)

# En Excel-fil med den aggregerade försäljningen.
grouped.to_excel("aggregated_sales.xlsx")

# Läs dem 5 första raderna:
print(df.head())

# Bonus uppdrag
# 1. Skapa en ny kolumn Discounted Sales där varje försäljning minskas med 10%.
# 2. Filtrera produkter där Discounted Sales > 400.
# 3. Exportera resultatet till en ny Excel-fil med namnet discounted_sales.xlsx.


# Lägg till rabatterad försäljning
df["Discounted Sales"] = df["Total Sales"] * 0.9

# Filtrera
discounted_df = df[df["Discounted Sales"] > 400]

# Exportera
discounted_df.to_excel("discounted_sales.xlsx", index=False)


