# Övningar

## Övning 1: Introduktion till maskininlärning – Linjär regression

Mål:
Förstå hur man implementerar en enkel linjär regression för att förutsäga försäljning baserat på marknadsföringskostnader.

Kodexempel:

```python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

# Exempeldataset
data = {
    "Marketing_Spend": [1000, 2000, 3000, 4000, 5000],
    "Sales": [12000, 25000, 37000, 45000, 52000]
}
df = pd.DataFrame(data)

# Dela upp data i input (X) och output (y)
X = df[["Marketing_Spend"]]
y = df["Sales"]

# Dela upp i tränings- och testdata
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Skapa och träna modellen
model = LinearRegression()
model.fit(X_train, y_train)

# Förutsägelser
y_pred = model.predict(X_test)

# Utvärdera modellen
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse}")

# Visualisera resultatet
plt.scatter(X_test, y_test, color="blue", label="Faktiska värden")
plt.plot(X_test, y_pred, color="red", label="Förutsägelse")
plt.xlabel("Marknadsföringskostnad")
plt.ylabel("Försäljning")
plt.legend()
plt.show()
```

## Övning 2: Klustring med k-means

Mål:
Identifiera kundgrupper baserat på region och försäljning.

Kodexempel:

```python
import pandas as pd
from sklearn.cluster import KMeans
import seaborn as sns
import matplotlib.pyplot as plt

# Exempeldataset
data = {
    "Region": [1, 2, 3, 1, 2, 3],
    "Sales": [100, 200, 150, 120, 180, 130]
}
df = pd.DataFrame(data)

# Skapa och träna k-means-modellen
kmeans = KMeans(n_clusters=2, random_state=42)
df["Cluster"] = kmeans.fit_predict(df[["Region", "Sales"]])

# Visualisera klustren
sns.scatterplot(x="Region", y="Sales", hue="Cluster", data=df, palette="deep")
plt.title("Kundkluster")
plt.xlabel("Region")
plt.ylabel("Försäljning")
plt.show()
```

## Övning 3: Förberedelse och hantering av data

Mål:
Arbeta med saknade värden och skapa nya kolumner.

Kodexempel:

```python
import pandas as pd

# Exempeldataset med saknade värden
data = {
    "Product": ["A", "B", "C", None],
    "Price": [100, None, 150, 200],
    "Quantity": [5, 10, None, 8]
}
df = pd.DataFrame(data)

# Hantera saknade värden
df["Price"].fillna(df["Price"].mean(), inplace=True)
df["Quantity"].fillna(1, inplace=True)

# Skapa en ny kolumn
df["Sales"] = df["Price"] * df["Quantity"]

print(df)
```

## Övning 4: Förutsäga försäljning med flera variabler

Mål:
Bygga en linjär regressionsmodell med flera oberoende variabler.

Kodexempel:

```python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# Exempeldataset
data = {
    "Marketing_Spend": [1000, 2000, 3000, 4000, 5000],
    "Region": [1, 2, 3, 1, 2],
    "Sales": [12000, 25000, 37000, 45000, 52000]
}
df = pd.DataFrame(data)

# Dela upp data
X = df[["Marketing_Spend", "Region"]]
y = df["Sales"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Skapa och träna modellen
model = LinearRegression()
model.fit(X_train, y_train)

# Förutsägelser
y_pred = model.predict(X_test)

# Utvärdera modellen
r2 = r2_score(y_test, y_pred)
print(f"R2 Score: {r2}")
```


## Övning 5: Visualisera distributionsdata

Mål:
Utforska datadistribution med Seaborn.

Kodexempel:

```python
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

# Generera data
data = np.random.normal(loc=50, scale=10, size=100)

# Histogram
sns.histplot(data, kde=True)
plt.title("Datafördelning")
plt.xlabel("Värde")
plt.ylabel("Frekvens")
plt.show()
```