from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pandas as pd
import numpy as np

all_houses = pd.read_csv("./all_houses.csv")

# Exempeldata från CSV-filen
# Address,Price,Size
# Kvadrantvägen 25,2000000,42

# Priser
X = all_houses["Size"]

# Storlek
y = all_houses[["Price"]]

# Ta bort alla värden efter + i t.ex: 118+8
X = X.str.split("+").str[0]
# Hantera svenska decimaler
X = X.str.replace(",", ".")

# Konvertera Series till DataFrame
X = X.to_frame()

# print(X)
# exit()
# print(y)

print("Modellträning...")
# Träna modellen
model = LinearRegression()
model.fit(X, y)

# Förutsäg ett nytt pris
# new_house = [[90]]

# För att undvika:
# UserWarning: X does not have valid feature names, but LinearRegression was fitted with feature names
# Måste vi skapa en DataFrame med rätt kolumnnamn
new_house = pd.DataFrame([[70]], columns=X.columns)

# Förutsäg priset för det nya huset
print("Förutspår")
predicted_price = model.predict(new_house)

# Avrunda till närmsta heltal
rounded_price = np.round(predicted_price)

print(f"Förväntat pris: {int(rounded_price.item())}kr")

