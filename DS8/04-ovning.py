"""
Installera först:
pip install pandas
pip install scikit-learn
pip install matplotlib

"""
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
