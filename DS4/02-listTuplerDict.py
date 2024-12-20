
# Skapa en lista med 5 namn.
# Lägg till ett namn och ta bort ett annat.
# Iterera genom listan och skriv ut alla namn.

print("Listor, tuppler och dictionaries")

# Listor:
names = ["Anna", "Bertil", "Cecilia", "David", "Eva"]
print(names)
names.append("Fredrik")
print(names)
names.remove("Bertil")
print(names)
for name in names:
    print(name)

# print(names)

# Tuppel för koordinater:
# Skapa en tuppel med tre koordinater (x, y, z).
# Försök att ändra ett värde och notera vad som händer.

coordinates = (1, 2, 3)
print(coordinates)

# Genererar ett felmeddelande
# coordinates[0] = 4
# print(coordinates)

# Dictionary för en produkt:
# Skapa en dictionary för en produkt med namn, pris och lager.
# Uppdatera lager och lägg till en nyckel för kategori.

product = {
    "name": "Bok",
    "price": 100,
    "stock": 5
}

print(product)

product["stock"] = 10
product["category"] = "Böcker"

print(product)

