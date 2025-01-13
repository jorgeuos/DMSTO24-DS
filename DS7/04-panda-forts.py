import pandas as pd

data = {
   "City": ["Stockholm", "Göteborg", "Stockholm", "Malmö"],
   "Sales": [100, 200, 150, 300]
}
df = pd.DataFrame(data)

grouped = df.groupby("City")["Sales"].sum()
print(grouped)





