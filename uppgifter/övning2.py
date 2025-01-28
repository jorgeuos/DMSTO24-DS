#Övning 2: Identifiera topprodukter

#Beskrivning:
#Testa att använda filtrering för att identifiera topprodukter med högst försäljning.

#Instruktioner:
#1. Skapa en ny kolumn Total_Sales genom att multiplicera pris och kvantitet.
#2. #Filtrera ut de produkter där Total_Sales är över 500.
#3. Spara dessa rader i en ny CSV-fil och skriv ut resultatet.

import pandas as pd
import matplotlib.pyplot as plt

# Läs in data
dataFrame = pd.read_csv("/Users/viktorheidmark/Documents/DMSTO24-DS/DS8/ovningar/fruits.csv")

# Skapa en ny kolumn för total försäljning
dataFrame["Total_Sales"] = dataFrame["Price"] * dataFrame["Quantity"]

# Filtrera produkter med hög försäljning
top_products = dataFrame[dataFrame["Total_Sales"] > 500]
print(top_products)

# Spara till en ny CSV-fil
top_products.to_csv("top_products.csv", index=False)