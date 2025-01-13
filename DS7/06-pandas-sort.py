import pandas as pd

data = {
   "Name": ["Fredrik", "Anna", "Björn", "Cecilia"],
   "Age": [23, 25, 30, 27],
   "City": ["Visby", "Stockholm", "Göteborg", "Malmö"]
}

df = pd.DataFrame(data)
# innan sortering:
print("Innan sortering:")
print(df)

# Efter sortering:
print("Efter sortering:")
df = df.sort_values(by="Age", ascending=False)
print(df)

# Sortera på namn:
print("Sortera på namn:")
df = df.sort_values(by="Name", ascending=False)
print(df)

