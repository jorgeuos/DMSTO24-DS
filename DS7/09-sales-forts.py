import pandas as pd
import matplotlib.pyplot as plt
"""
Se till att du har installerat både pandas och matplotlib
pip install pandas
pip install matplotlib
"""


# Läs filen sales-2.csv
df = pd.read_csv("sales-2.csv")
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


# Testa o rita en enkel graf:
# x = [1,2,3]
# y = [4,5,6]
# plt.plot(x,y)
# plt.title("Linjediagram")
# plt.xlabel("X-axeln")
# plt.ylabel("Y-axeln")


# Testa o rita en enkel graf 2:
# x = ["A","B","C"]
# y = [10,20,15]
# plt.bar(x,y)
# plt.title("Stapeldiagram")
# plt.xlabel("X-axeln")
# plt.ylabel("Y-axeln")
# plt.show()

print(data_with_cat)

# Det här funkar inte, för att groupby genererar en SERIES där index är Date
# dates = data_with_cat.groupby("Date")["Sales"].sum()["Date"]

# Så vi måste antingen, hämta dates med unique()
# dates = data_with_cat["Date"].unique()

# Eller hämta indexet som är date:
dates = data_with_cat.groupby("Date")["Sales"].sum().index
sales_per_date = data_with_cat.groupby("Date")["Sales"].sum()

# x = dates
# y = sales_per_date

# plt.plot(x, y)
# plt.title("linje")
# plt.xlabel("Datum")
# plt.ylabel("Försäljning")
# plt.show()

# Testa lägga in fler rader
# banan melon kiwi och citron

# Skapa nya rader
new_row1 = {"Date": "2023-01-04", "Banan": "", "Price": 12, "Quantity": 60, "Category": "Fruit"}
new_row2 = {"Date": "2023-01-05", "Melon": "", "Price": 6, "Quantity": 150, "Category": "Fruit"}
new_row3 = {"Date": "2023-01-06", "Kiwi": "", "Price": 20, "Quantity": 80, "Category": "Fruit"}
new_row4 = {"Date": "2023-01-07", "Citron": "", "Price": 15, "Quantity": 60, "Category": "Fruit"}

# Lägg till raderna i data_with_cat
data_with_cat.loc[len(data_with_cat)] = new_row1
data_with_cat.loc[len(data_with_cat)] = new_row2
data_with_cat.loc[len(data_with_cat)] = new_row3
data_with_cat.loc[len(data_with_cat)] = new_row4

# Beräkna sales igen
data_with_cat["Sales"] = data_with_cat["Price"] * data_with_cat["Quantity"]

# Ta fram x och y
x = data_with_cat.groupby("Date")["Sales"].sum().index
y = data_with_cat.groupby("Date")["Sales"].sum()

# Rita grafen
plt.plot(x, y)
plt.title("linje")
plt.xlabel("Datum")
plt.ylabel("Försäljning")
plt.show()
