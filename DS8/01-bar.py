import pandas as pd
import matplotlib.pyplot as plt
"""
Se till att du har installerat både pandas och matplotlib
pip install pandas
pip install matplotlib
"""


# Läs filen sales.csv
df = pd.read_csv("sales.csv")
print(df)

# Summera på price
print("Summera på price")
sum_price = df["Price"].sum()
print(sum_price)


print("hasNaN")
hasNaN = df["Price"].isna()
print(hasNaN)


# Hur många null värden finns det i tabellen
print("isNull")
isNull = df["Price"].isnull().sum()
print(isNull)

# Raderar rader som saknar pris
print("drop")
drop = df["Price"].dropna()
print(drop)

# Lägg till kolumn Category
data_with_cat = df
data_with_cat["Category"] = "Fruit"

print("data_with_cat")
print(data_with_cat)

# Beräkna sales
data_with_cat["Sales"] = data_with_cat["Price"] * data_with_cat["Quantity"]

# # Eller hämta indexet som är date:
datesAndSales = data_with_cat.groupby("Date")["Sales"].sum()

# Skapa nya rader
new_row1 = {
    "Date": "2023-01-04",
    "Product": "Banan",
    "Price": 12,
    "Quantity": 60,
    "Category": "Fruit"
    }
new_row2 = {"Date": "2023-01-05", "Product": "Melon", "Price": 6, "Quantity": 150, "Category": "Fruit"}
new_row3 = {"Date": "2023-01-06", "Product": "Kiwi", "Price": 20, "Quantity": 80, "Category": "Fruit"}
new_row4 = {"Date": "2023-01-07", "Product": "Citron", "Price": 15, "Quantity": 60, "Category": "Fruit"}

# Lägg till raderna i data_with_cat
data_with_cat.loc[len(data_with_cat)] = new_row1
data_with_cat.loc[len(data_with_cat)] = new_row2
data_with_cat.loc[len(data_with_cat)] = new_row3
data_with_cat.loc[len(data_with_cat)] = new_row4

# Beräkna sales igen
data_with_cat["Sales"] = data_with_cat["Price"] * data_with_cat["Quantity"]

# # Ta fram x och y
# x = data_with_cat.groupby("Date")["Sales"].sum().index
# y = data_with_cat.groupby("Date")["Sales"].sum()

# Eller kortare:
xANDy = data_with_cat.groupby("Product")["Quantity"].sum()

print(xANDy)

# Spara som en kalkylerad csv fil
# data_with_cat.to_csv("data_with_cat.csv")

# Rita grafen
plt.bar(xANDy.index, xANDy.values)
plt.title("Stapeldiagram")
plt.xlabel("Frukt")
plt.ylabel("Antal")
plt.show()
