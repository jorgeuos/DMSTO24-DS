# Fördjupning av TXT-filer


1. Läsning och skrivning rad för rad

Varför? Förstå hur man arbetar med stora filer eller bearbetar text rad för rad.

Exempel:
	•	Läs en fil rad för rad och skriv ut varje rad med radnummer:

```python
with open("example.txt", "r") as file:
    for i, line in enumerate(file, start=1):
        print(f"Rad {i}: {line.strip()}")
```
	•	Övning: Skriv en funktion som läser en fil och returnerar antalet rader i den.

2. Sökning i textfiler

Varför? Introducerar filtrering och specifik sökning, vilket kopplar till dataanalys.

Exempel:
	•	Sök efter en specifik sträng i en fil och skriv ut raderna där den förekommer:

```python
keyword = "Python"
with open("example.txt", "r") as file:
    for line in file:
        if keyword in line:
            print(line.strip())
```

	•	Övning: Skriv ett program som letar efter flera nyckelord och skriver ut resultaten.

3. Rensa och transformera textdata

Varför? Förstå att data ofta behöver bearbetas innan det kan analyseras.

Exempel:
	•	Läs en fil och rensa bort tomma rader eller rader som börjar med en kommentar (#):

```python
cleaned_lines = []
with open("example.txt", "r") as file:
    for line in file:
        if line.strip() and not line.startswith("#"):
            cleaned_lines.append(line.strip())

print(cleaned_lines)
```

	•	Övning: Skapa en funktion som rensar texten och sparar den till en ny fil.

4. Lagra data i listor

Varför? Förberedande för att övergå till strukturerade format som CSV.

Exempel:
	•	Läs en fil och lagra varje rad som en lista:

```python
lines = []
with open("example.txt", "r") as file:
    lines = [line.strip() for line in file]

print(lines)
```

	•	Övning: Omvandla varje rad till en lista av ord (använd split()).

5. Spara bearbetad text till en ny fil

Varför? Ger en praktisk tillämpning av att skriva data till en fil.

Exempel:
	•	Läs en fil, rensa data, och spara den till en ny fil:

```python
with open("example.txt", "r") as infile, open("cleaned_example.txt", "w") as outfile:
    for line in infile:
        if line.strip():
            outfile.write(line.strip() + "\n")
```

	•	Övning: Skapa ett program som kopierar innehållet från en fil till en annan och lägger till radnummer.

6. Kombinera flera textfiler

Varför? Introducerar arbete med flera filer, vilket är en vanlig uppgift i filhantering.

Exempel:
	•	Kombinera innehåll från flera filer till en ny fil:

```python
filenames = ["file1.txt", "file2.txt"]
with open("combined.txt", "w") as outfile:
    for fname in filenames:
        with open(fname, "r") as infile:
            outfile.write(infile.read() + "\n")
```

	•	Övning: Kombinera tre textfiler och sortera raderna i alfabetisk ordning innan du sparar.

7. Identifiera och hantera saknade värden

Varför? Förberedelse för att hantera saknade data i CSV-filer.

Exempel:
	•	Markera rader som saknar viss information:

```python
with open("example.txt", "r") as file:
    for line in file:
        if not line.strip():
            print("Tom rad hittad!")
```

	•	Övning: Hitta rader som innehåller mindre än tre ord.

Sammanfattning av vad som kan visas
	•	Grundläggande läsning och skrivning (rad för rad, hela filen).
	•	Rensa och filtrera textdata.
	•	Lagra data i listor.
	•	Bearbeta data och spara till nya filer.
	•	Arbeta med flera filer (kombinera och sortera).
