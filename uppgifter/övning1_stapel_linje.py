#Övning 1: Analysera försäljningsdata
#Gruppera och analysera försäljningsdata, samt skapa stapeldiagram och
#linjediagram.
#Instruktioner:
#1. Läs in filen fruits.csv.
#2. Gruppera data baserat på produkt och summera försäljningen.
#3. Skapa följande grafer:
# Ett stapeldiagram som visar total försäljning per produkt.
# Ett linjediagram som visar försäljningen över tid för varje produkt.




import pandas as pd
import matplotlib.pyplot as plt

# Läs in data
dataFrame = pd.read_csv("/Users/viktorheidmark/Documents/DMSTO24-DS/DS8/ovningar/fruits.csv")

# Gruppera och summera försäljning per produkt
grouped_data = dataFrame.groupby("Product").sum("Sales")
print(grouped_data)
# Skapa ett stapeldiagram
plt.bar(grouped_data.index, grouped_data["Sales"])
plt.title("Total försäljning per produkt")
plt.xlabel("Produkt") 
plt.ylabel("Försäljning")
plt.show()

# Gruppera och summera försäljning över tid i ett linjediagram  
time_series = dataFrame.groupby("Date").sum("Sales")
plt.plot(time_series.index, time_series["Sales"])
plt.title("Försäljning över tid")
plt.xlabel("Datum")
plt.ylabel("Försäljning")
plt.show()

