import pandas as pd
import matplotlib.pyplot as plt

# Läs in data
dataFrame = pd.read_csv("fruits.csv")

# Gruppera baserat på kategori
category_data = dataFrame.groupby("Product").sum("Sales")
print(category_data)

# Cirkeldiagram
labels = 'IT', 'Marketing', 'Data Science', 'Finance'
values = [500, 156, 300, 510]
explode = (0.05, 0.05, 0.05, 0.05) 
# explode = (0.05, 0.05, 0.05, 0.05,0.05, 0.05, 0.05, 0.05,0.05, 0.05, 0.05, 0.05)
print(len(category_data["Sales"]))
# plt.pie(category_data["Sales"], labels=category_data.index, autopct="%1.1f%%", explode=explode, shadow=True)
plt.pie(values, labels=labels, autopct="%1.1f%%", shadow=True, explode=explode)
# plt.Color = 'green'

plt.title("Fördelning av försäljning per kategori")
plt.legend()
plt.show()

# def plot(**kwargs):
#     for key, val in kwargs.items():
#         plt.plot(val, label=key)
#     plt.legend()
#     plt.tight_layout()
#     # plt.savefig('train_loss_vs_beta.pdf')
#     plt.show()

# Histogram för kvantitet
plt.hist(dataFrame["Quantity"], bins=10)
plt.title("Fördelning av kvantitet")
plt.xlabel("Kvantitet")
plt.ylabel("Frekvens")
plt.show()

# Ett scatter plot som visar relationen mellan pris och kvantitet.
plt.scatter(dataFrame["Price"], dataFrame["Quantity"])
plt.title("Relation mellan pris och kvantitet")
plt.xlabel("Pris")
plt.ylabel("Kvantitet")
plt.show()

