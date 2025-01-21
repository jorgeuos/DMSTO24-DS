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

# Skapa histogram för varje kluster och kön
clusters = people_income["Cluster"].unique()
genders = people_income["Gender"].unique()

plt.figure(figsize=(10, 6))
for cluster in clusters:
    for gender in genders:
        cluster_gender_data = people_income[
            (people_income["Cluster"] == cluster) & (people_income["Gender"] == gender)
        ]
        plt.hist(
            cluster_gender_data["Income"],
            bins=20,
            alpha=0.5,
            label=f"Kluster {cluster} - {gender}",
        )

# Anpassa histogrammet
plt.title("Inkomstfördelning per kluster och kön")
plt.xlabel("Inkomst")
plt.ylabel("Antal personer")
plt.legend()
plt.grid(True)

# Visa diagrammet
plt.show()