import pandas as pd

# Kör först i terminal fönstret(om du inte gjort det redan):
"""
$ pip install pandas
"""

# print(pd.__version__)

# Hemläxa Jorge: Dokumentera med kommentarer!!!


data = {
   "Name": ["Anna", "Björn", "Cecilia"],
   "Age": [25, 30, 27],
   "City": ["Stockholm", "Göteborg", "Malmö"]
}

df = pd.DataFrame(data)

print(df)

df = df.sort_values(by="Age", ascending=False)

