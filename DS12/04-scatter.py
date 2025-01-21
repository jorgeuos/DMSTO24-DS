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

# Skapa scatter plot för varje kön inom varje kluster
plt.figure(figsize=(12, 8))

# Symboler för olika kön
markers = {"Kvinna": "o", "Man": "^"}

for cluster in people_income["Cluster"].unique():
    for gender, marker in markers.items():
        cluster_gender_data = people_income[
            (people_income["Cluster"] == cluster) & (people_income["Gender"] == gender)
        ]
        plt.scatter(
            cluster_gender_data["Age"],
            cluster_gender_data["Income"],
            marker=marker,
            label=f"Kluster {cluster} - {gender}",
            alpha=0.7
        )

# Anpassa ploten
plt.title("Klusterdiagram: Ålder vs Inkomst med könsfördelning")
plt.xlabel("Ålder")
plt.ylabel("Inkomst")
plt.legend()
plt.grid(alpha=0.3)

# Visa ploten
plt.show()