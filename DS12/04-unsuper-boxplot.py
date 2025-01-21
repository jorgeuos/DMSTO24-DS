import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cluster import KMeans

# Läs in data
people_income = pd.read_csv("./syntetisk_inkomstdata.csv")

# Välj data att klustra
data = people_income[["Age", "Income"]]

# Träna klustringsmodellen
kmeans = KMeans(n_clusters=2, random_state=42)
kmeans.fit(data)

# Lägg till kluster som en ny kolumn
people_income["Cluster"] = kmeans.labels_

# Skapa en kolumn som kombinerar kön och kluster för visualisering
people_income["Cluster_Gender"] = (
    "Kluster " + people_income["Cluster"].astype(str) + " - " + people_income["Gender"]
)

# Skapa en boxplot
plt.figure(figsize=(12, 6))
people_income.boxplot(
    column="Income", by="Cluster_Gender", grid=False, showmeans=True, meanline=True
)

# Anpassa boxploten
plt.title("Inkomstfördelning per kluster och kön")
plt.suptitle("")  # Ta bort standardtitel som genereras av pandas
plt.xlabel("Kluster och kön")
plt.ylabel("Inkomst")
plt.xticks(rotation=45)
plt.grid(axis="y", linestyle="--", alpha=0.7)

# Visa ploten
plt.show()
