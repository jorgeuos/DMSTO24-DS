import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import pandas as pd

# Läs in data
people_income = pd.read_csv("./syntetisk_inkomstdata.csv")

# Exempeldata
# Age,Gender,Income
# 25,Kvinna,315089.06
# 58,Man,418269.6

# Välj data att klustra
data = {
    "Age": people_income["Age"],
    "Income": people_income["Income"]
}
df = pd.DataFrame(data)

# print(df)

# Träna klustringsmodellen
kmeans = KMeans(n_clusters=2, random_state=42)
kmeans.fit(df)

# Gruppera kunder
df["Cluster"] = kmeans.labels_
print(df)

# Lägg till kluster som en ny kolumn
people_income["Cluster"] = kmeans.labels_

# Generera histogram för varje kluster
for cluster in range(2):  # Antal kluster
    cluster_data = people_income[people_income["Cluster"] == cluster]
    plt.hist(cluster_data["Income"], bins=20, alpha=0.5, label=f"Cluster {cluster}")



# Anpassa histogrammet
plt.title("Inkomstfördelning per kluster")
plt.xlabel("Inkomst")
plt.ylabel("Antal personer")
plt.legend()
plt.grid(True)

# Visa diagrammet
plt.show()
