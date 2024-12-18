"""
Övning: Listor
Skapa och manipulera en lista:
Skapa en lista med 5 städer.
Lägg till en ny stad i slutet av listan.
Ta bort den andra staden i listan.
Skriv ut alla städer med en for-loop.

Lagra och summera heltal:
Skapa en lista med 5 heltal.
Summera alla tal i listan.

Utmaning:
Skapa en lista med namn och sök efter ett namn med en for-loop.
Uppdatera alla städer till stor begynnelsebokstav
"""

cityList = ["stockholm", "göteborg", "malmö", "uppsala", "västerås"]
print("Hela cityList")
print(cityList)

print("cityList append")
cityList.append("london")
print(cityList)

print("cityList pop")
cityList.pop(1)
print(cityList)

print("cityList del")
del cityList[1]
print(cityList)

print("cityList for")
for item in cityList:
    print(item)

numList = [1,2,3,4,5]

print("Lista med Heltal")
print(numList)

print("Summa Heltal med sum")
summa = sum(numList)
print(summa)

print("Summa Heltal med for")
x = 0
for i in numList:
    x = x + i
print(x)

print(sum(numList))


nameList = ["Beneretta", "Johan", "Lucy", "Malin"]
print(nameList)
for name in nameList:
    search = "Johan"
    if name == search:
        print("Hittade " + name)
        break
    else:
        print("Hittade inte " + search)

print("Uppdatera alla städer till stor begynnelsebokstav:")
print(cityList)
for i, city in enumerate(cityList):
    print(city.capitalize())
    cityList[i] = city.capitalize()

print(cityList)

cityList = ["stockholm", "göteborg", "malmö", "uppsala", "västerås"]
newCityList = []

print("Uppdatera med list:")
for city in cityList:
    cityDrawer = list(city)
    firstLetter = cityDrawer[0]
    capitalized = firstLetter.upper()
    cityDrawer[0] = capitalized
    # city[0] = capitalized
    
    city = "".join(cityDrawer)
    # Blir väldigt spännande om vi castar till str
    # city = str(cityDrawer)
    newCityList.append(city)
    print(city)

# cityList = newCityList
# newCityList = None

print(cityList)
print(newCityList)


