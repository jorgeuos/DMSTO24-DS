"""
Filhantering i Python:
Öppna, läsa, skriva och stänga filer.
Hantera CSV-filer med inbyggda bibliotek.
Pandas:
Introduktion och grunder
DataFrames:
Vad de är och varför de är användbara.
Grundläggande operationer som att manipulera kolumner och filtrera data.
Kombinera filhantering och Pandas:
Läsa, bearbeta och exportera data i olika format (CSV och Excel).
"""
"""
För att exekvera denna fil med python.
1. Navigera till mappen DS7
cd DS7
2. Kör python scriptet:
python 01-recap.py
"""


print("Hello, World!")

# Öppna en fil med context manager(i skrivläge = w):
with open("data.csv", "w") as file:
    # Vi skriver till filen, rad 1, rubrikerna:
    file.write("Name,Age,City\n")
# Nu är filen stängd

# Vi öppnar filen igen, med append
with open("data.csv", "a") as file:
    # Men kom ihåg att lägga till ett radbryt \n
    file.write("Anna,25,Stockholm\n")
    file.write("Björn,30,Göteborg\n")
    file.write("Cecelia,27,Stockholm")
    # Filen stängs när jag börjar nytt kodblock neda:

# Öppna i läsläge
with open("data.csv") as file:
    # Skriv ut innehållet
    print(file.read())

print("Rad för rad:")
# Vi kanske vill jobba rad för rad
with open("data.csv") as file:
    # Loopa igenom rad för rad
    for line in file:
        # Do something...
        # Strip tar bort den extra radbrytningen
        print(line.strip())
        letaEfter = "Cecelia"
        if letaEfter in line:
            print(f"{letaEfter} är bäst!")
            print(f"Hela raden: {line}")
