# Börja med att installera pandas:
# pip install pandas
# eller
# python -m pip install pandas
"""
Exekvera filen med:
python 03-pandas.py
"""

# 2. importera pandas
import pandas as pd

# 3. Kolla att pandas fungerar:
print(pd.__version__)

# 4. Skapa en DataFrame med Pandas

# Data en dictionary med nyckel för column rubrik
# och lista på värden per rad
data = {
   "Name": ["Anna", "Björn", "Cecilia"],
   "Age": [25, 30, 27],
   "City": ["Stockholm", "Göteborg", "Malmö"]
}

df = pd.DataFrame(data)

print(df)
print(df.info())



# Gör något med kolumnen Age
print("Gör något med kolumnen Ages:")
ages = df["Age"]
print(ages)

print("Alla äldre än 25:")
filtered_data = df[df["Age"] > 25]
print(filtered_data)

print("Alla yngre än eller exakt 25 år:")
filtered_data = df[df["Age"] <= 25]
print(filtered_data)

# Summera alla åldrar i kolumnen Age
summa = df["Age"].sum()
# Räknar antal rader
antal = df["Age"].count()
print(summa)
print(antal)

# vi gör en beräkning:
print("Egen beräkning:")
print(summa/antal)

# eller vi använder inbyggda funktioner
print("Inbyggd beräkning för medelvärde:")
print(df["Age"].mean())

print("Eller median:")
print(df["Age"].median())



