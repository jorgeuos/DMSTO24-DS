import pandas as pd
import matplotlib.pyplot as plt

dataFrame = pd.read_csv("data_with_cat.csv")
print(dataFrame)

# notAvailable = dataFrame.isna()
# print(notAvailable)

xY = dataFrame.groupby("Product").sum("Sales")
print(xY)

plt.bar(xY.index, xY.get("Sales"), label = 'En Label')
plt.title("Stapeldiagram av Frukter och Total försäljning", loc="right")

plt.legend(loc='lower center')

plt.show()
