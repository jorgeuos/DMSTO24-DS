import csv
"""
För att exekvera denna fil med python.
1. Navigera till mappen DS7
cd DS7
2. Kör python scriptet:
python 02-recap-csv.py
"""


print("Rad för rad:")
with open("data.csv", "r") as file:
   reader = csv.reader(file)
   for row in reader:
       print(row)

print("Read as dictionary:")
with open("data.csv", "r") as file:
    # csv reader hanterar radbryt åt mig
    reader = csv.DictReader(file)
    letaEfter = "Cecelia"
    summanAvAllaAldrar = 0
    listaAvAllaAldrar = []
    # Loopar igenom alla rader
    for row in reader:
        # Behöver inte ta bort radbryt (strip)
        # Vi matchar letarEfter med nyckeln "Name" i vår dictionary:
        if letaEfter in row.get("Name"):
            # Skriv ut värdet(value)
            # i vår nyckel/värde-par
            print(f"Hej {row.get("Name")}")
            print(f"Som är {row.get("Age")} gammal...")
            # Vi kan även göra beräkningar med att summera alla åldrar:
        # Vi går ur if-villkoret
        # Vi summerar ålder som en int till vår behållare summanAvAllaAldrar
        summanAvAllaAldrar += int(row.get("Age"))
        # Vi kan även lägga alla åldrar i en lista, för att göra beräkningar på:
        listaAvAllaAldrar.append(int(row.get("Age")))
    # Vi går ur for-loopen
    # Summan är nu räknad, utanför for-loopen
    print(f"Summan av alla åldrar: {summanAvAllaAldrar}")
    # Vi skriver ut vår lista, för att se vad vi har:
    print(listaAvAllaAldrar)

    # Vi kan använda de inbyggda funktionerna, sum() delat med len()
    print(sum(listaAvAllaAldrar))
    print(len(listaAvAllaAldrar))
    # Medelvärde
    average = round(sum(listaAvAllaAldrar)/len(listaAvAllaAldrar))
    print(f"Medelvärde på åldrar: {average}")




