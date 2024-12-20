
# myfamily = {
#   "child1" : {
#     "name" : "Emil",
#     "year" : 2004,
#     "hobbies": ["Programming", "Football", "Gaming"]
#   },
#   "child2" : {
#     "name" : "Tobias",
#     "year" : 2007
#   },
#   "child3" : {
#     "name" : "Linus",
#     "year" : 2011
#   }
# }

# print( len(myfamily) )

# print(myfamily)

# print(f'{", ".join(myfamily["child1"]["hobbies"])}')

produkt = {
    "namn": "Laptop",
    "pris": 10000,
    "lager": 50
}


# 1. Skriv ut produktens pris.
print(produkt["pris"])
# 2. Lägg till en nyckel för "kategori".
produkt["kategori"] = "Datorer"
print(produkt)
# 3. Ändra värdet på "lager" till 40.
produkt["lager"] = 40
print(produkt)


# Skapa en dictionary med tre nyckel-värde-par (e.g., "namn", "ålder", "stad").
# Iterera genom dictionaryn och skriv ut varje nyckel och värde.
# Ex:
person = {"name": "Anna", "age": 25, "city": "Stockholm"}
# ... fortsätt här

print(type(person))

for key, value in person.items():
    print(f'Personens {key} är {value}')

print(person.items())
# class Dictionary:
#     def __init__(self, dictionary):
#         self.dictionary = dictionary

#     def items(self):
#         for key, value in self.dictionary.items():
#             yield key, value