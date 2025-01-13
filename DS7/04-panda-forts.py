import pandas as pd

data = {
   "City": ["Stockholm", "Göteborg", "Stockholm", "Malmö"],
   "Sales": [100, 200, 150, 300]
}
df = pd.DataFrame(data)

grouped = df.groupby("City")["Sales"].sum()
print(grouped)



# Från DS6 - Lägga till kolumner
data = {
   "Name": ["Anna", "Björn", "Cecilia"],
   "Age": [25, 30, 27],
   "City": ["Stockholm", "Göteborg", "Malmö"]
}

df2 = pd.DataFrame(data)

# Lägg till en ny kolumn
df2["Age_in_10_years"] = df2["Age"] + 10
print(df2)

# Ta bort en kolumn
print("Utan kolumn city")
df2 = df2.drop(columns=["City"])
print(df2)



