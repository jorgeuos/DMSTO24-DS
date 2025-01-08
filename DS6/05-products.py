
import csv
"""
Läs filen och skriv ut innehållet rad för rad.
Skapa en ny CSV-fil som innehåller:
Samma data, men med en extra kolumn för "Category".
"""


# with open("products.csv", "r") as file:
#     reader = csv.reader(file)
#     for row in reader:
#         row.append("Category")
#         print(row)

with open("products.csv", "r") as file:
    reader = csv.reader(file)
    data = list(reader)

# [["Name", "Price"], ["Apple", 10], ["Banana", 5], ["Cherry", 20]]
data[0].append("Category")

for i in range(1, len(data)):
    data[i].append("Fruits")

for i in range(len(data)):
    print(data[i])

with open("new-products.csv", "w") as new_products:
    writer = csv.writer(new_products)
    writer.writerows(data)


