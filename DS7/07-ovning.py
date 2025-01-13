import pandas as pd

"""
Övning från DS6:
Skapa en ny kolumn Total Value (Price * Stock).
Spara resultatet i en ny Excel-fil med namnet products_analysis.xlsx.

Ger error om du inte installerar:
pip install openpyxl
"""

# Läs CSV
df = pd.read_csv("products.csv")

# Lägg till ny kolumn
df["Total Value"] = df["Price"] * df["Stock"]

# Skriv till Excel
df.to_excel("products_analysis.xlsx", index=False, sheet_name="Analysis")

