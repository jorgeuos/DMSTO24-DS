import pandas as pd
import matplotlib.pyplot as plt

# Läs in data
dataFrame = pd.read_csv("fruits.csv")

# Kontrollera saknade värden
print(dataFrame.isnull().sum())

# Fyll i saknade värden
dataFrame["Price"].fillna(dataFrame["Price"].mean(), inplace=True)
dataFrame["Quantity"].fillna(0, inplace=True)

print("Efter att saknade värden har fyllts i:")
print(dataFrame)


