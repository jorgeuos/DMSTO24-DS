#Övning 3: Visualisera kategoridata

#Beskrivning:
#Testa att skapa visualiseringar som jämför försäljningen mellan olika kategorier.

#Instruktioner:
#1.Gruppera data baserat på column(kanske inte frukt) och summera
#försäljningen. Product kolumnen ger ett roligare diagram.

#2.Skapa ett cirkeldiagram (pie chart) för att visa fördelningen av försäljning mellan kategorierna.

#3.Skapa ett histogram som visar fördelningen av kvantitet (Quantity).

import pandas as pd
import matplotlib.pyplot as plt


# Läs in data
dataFrame = pd.read_csv("/Users/viktorheidmark/Documents/DMSTO24-DS/DS8/ovningar/fruits.csv")

# Gruppera baserat på kategori
category_data = dataFrame.groupby("Product").sum("Sales")
print(category_data)

# Histogram för kvantitet
plt.hist(dataFrame["Quantity"], bins=10)
plt.title("Fördelning av kvantitet")
plt.xlabel("Kvantitet")
plt.ylabel("Frekvens")
plt.show()
