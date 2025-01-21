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

# Skapa scatter plot
plt.figure(figsize=(10, 6))
for cluster in people_income["Cluster"].unique():
    cluster_data = people_income[people_income["Cluster"] == cluster]
    plt.scatter(
        cluster_data["Age"],
        cluster_data["Income"],
        label=f"Kluster {cluster}",
        alpha=0.7
    )

# Anpassa ploten
plt.title("Klusterdiagram: Ålder vs Inkomst")
plt.xlabel("Ålder")
plt.ylabel("Inkomst")
plt.legend()
plt.grid(alpha=0.3)

# Visa ploten
plt.show()