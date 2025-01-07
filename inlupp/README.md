# Instruktioner för inlämningsuppgift 1

## Inlämning

Inlämningen sker genom att du pushar dina ändringar till ditt repository på GitHub. Du ska alltså inte skicka in något via Teams eller mail förutom länken till ditt repo i Learnpoint. Se till att du har pushat alla dina ändringar innan deadline.

```bash
git add -A
git commit -m "Din commit message här"
git pull origin main
# eller master beroende på vilken branch du jobbar på
git push origin main
```

Jag har förberett med automatiska tester för varje uppgift. Dessa tester kommer att kontrollera att din lösning är korrekt. Om testerna inte passerar kommer du att få ett felmeddelande som säger att testerna har misslyckats. Du kan köra testerna genom att använda kommandot `pytest` i terminalen.

## Pytest

För att kunna testa lösningarna på dina uppgifter behöver du först installera `pytest`. Det gör du genom att köra kommandot:

```bash
pip install pytest
```

Alternativt kan du använda `pip3`:

```bash
pip3 install pytest
```
### Om `pytest` inte fungerar

Testa köra:

```bash
python -m pytest test_exempel_1.py
```

## Lösa uppgifter

I varje mapp så ligger det en uppgift som du ska lösa. Uppgiften är beskriven i en README-fil i mappen. Läs igenom uppgiften och skriv din lösning i filen `uppgift_(UPPGIFTS_NUMMER).py` i samma mapp som README-filen för uppgiften.

Modifiera EJ testfilen `test_uppgift_(UPPGIFTS_NUMMER).py`. Denna fil innehåller testfall som kommer att användas för att kontrollera att din lösning är korrekt och den är samma för alla.

Döp inte om filerna, då kommer testerna inte att fungera heller. Anledningen till att filerna har understreck i sina namn är för att bindessträck och mellanslag inte är tillåtna i filnamn vid importering av moduler i Python.

## Testa uppgifterna

För att testa din lösning kör du kommandot `pytest` i samma mapp som din lösning ligger i. Om du har gjort uppgiften korrekt ska du se utskrifter i terminalen som säger att testerna har passerats.


Det ska alltså bli grönt om testerna har passerats och rött om testerna har misslyckats.
<img src="../bilder/fail-pass.png" alt="fail-pass" width="500"/>

## Navigera till mappen

För att navigera till mappen där uppgiften ligger kan du använda kommandot `cd`(change directory). Exempel:

```bash
cd inlupp/exempel
```

För att kontrollera att du är i rätt mapp kan du använda kommandot `ls`(list) för att lista alla filer och mappar i den mappen.

```bash
ls
# Output: README.md __pycache__ exempel_1.py test_exempel_1.py
```

Ni kan ignorera filen/mappen `__pycache__` då den skapas automatiskt av Python när ni kör era program.

Annars kan du använda kommandot `pwd`(print working directory) för att skriva ut vilken mapp du är i.

```bash
pwd
# Rätt mapp:
# Output: /Users/jorge/projects/tuc/DataScience/inlupp/exempel
# Fel mapp:
# Output: /Users/jorge/projects/tuc/DataScience/inlupp
```

I windows ser det snarare ut såhär:

```bash
pwd
# Output:
# C:\Users\jorge\projects\tuc\DataScience\inlupp\exempel
```

## Navigera tillbaka

För att navigera tillbaka en mapp kan du använda kommandot `cd ..`. Exempel:

```bash
cd ..
```

`..` (punkt punkt) betyder att du går tillbaka en mapp. Om du skriver `cd ../..` så går du tillbaka två mappar.

Alternativt kan du skriva hela sökvägen till mappen du vill gå till. Exempel:

```bash
cd /Users/jorge/projects/tuc/DataScience/inlupp/uppgift_1
```

Observera att sökvägen kan se annorlunda ut beroende på var du har lagt mappen `inlupp` på din dator eller om du använder Windows vs Mac/Linux.

## Uppgift 1

Skapa en funktion is_odd(x) som returnerar True om x är udda och False om x är jämnt.

### Beskrivning

Skapa en funktion `is_odd(x: int) -> bool` som returnerar True om x är udda och False om x är jämnt.

### Funktionens Signatur

```python
def is_odd(x: int) -> bool:
    """
    Returnerar True om x är udda, annars False.
    """
    pass # Ta bort denna rad och skriv din kod här
```

## Uppgift 2

Summera alla siffror i en lista

### Beskrivning

Skapa en funktion sum_list(numbers) som returnerar summan av alla siffror i listan.

### Funktionens Signatur

```python
def sum_list(numbers: List[int]) -> int:
    """
    Returnerar summan av alla siffror i listan.
    """
    pass # Ta bort denna rad och skriv din kod här
```

## Uppgift 3

Hitta det största talet i en lista

### Beskrivning

Skapa en funktion max_in_list(numbers) som returnerar det största talet i listan.

### Funktionens Signatur

```python
def max_in_list(numbers: List[int]) -> int:
    """
    Returnerar det största talet i listan.
    """
    pass # Ta bort denna rad och skriv din kod här
```

## Uppgift 4

Fibonacci’s talföljd är en talföljd där varje tal är summan av de två föregående talen. Talföljden börjar med 0 och 1. De första talen i talföljden är:

```
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
```

### Beskrivning

Skriv en funktion `fibonacci(n: int) -> List[int]` som returnerar en lista med de `n` första talen i Fibonacci’s talföljd.

### Exempel

```python
>>> fibonacci(10)
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
```

## Uppgift 5

Filtrera udda tal från en lista

### Beskrivning

Instruktion: Skapa en funktion filter_odd(numbers) som returnerar en lista med alla jämna tal från den givna listan.

## Uppgift 6

Skapa multiplikationstabellen

### Beskrivning

Skapa en funktion multiplication_table(n, limit) som returnerar multiplikationstabellen för n upp till limit i en lista.

## Uppgift 7

Validera ett lösenord

### Beskrivning

Skapa en funktion validate_password(password) som kontrollerar att lösenordet är minst 8 tecken långt och innehåller minst en siffra.

## Uppgift 8

Räkna förekomsten av bokstäver

### Beskrivning

Skapa en funktion count_letters(string) som returnerar en dictionary med varje bokstav som nyckel och antalet förekomster som värde.

## Uppgift 9

Palindromkontroll

### Beskrivning

Skapa en funktion is_palindrome(string) som kontrollerar om en given sträng är ett palindrom (dvs. samma framifrån och bakifrån).



## Uppgift 10

Konvertera celsius till fahrenheit

### Beskrivning

Skapa en funktion celsius_to_fahrenheit(celsius) som konverterar en temperatur från Celsius till Fahrenheit.

## Uppgift 11

Räkna orden i en text

### Beskrivning

Skapa en funktion word_count(text) som returnerar antalet ord i en given text.

## Uppgift 12

Lagra data i en dictionary

### Beskrivning

Skapa en funktion create_student_register(students) som tar emot en lista med namn och ålder och returnerar en dictionary där namnet är nyckeln och åldern är värdet.


## Tips och tricks

- Läs uppgiften noga och försök förstå vad som efterfrågas.
- Skriv pseudokod för att förstå hur du ska lösa uppgiften.
- Kolla testfallen för att förstå vad som förväntas av din lösning.
- Använd `print()` för att felsöka och för att skriva ut värden så att du vet att din lösning fungerar som den ska.
- Googla om du fastnar. Det finns mycket information på internet som kan hjälpa dig.
- Fråga om hjälp i Teams om du behöver det. Det finns alltid någon som kan hjälpa dig.
- Kom ihåg att det är okej att göra fel. Det är en del av lärandeprocessen.
- Testa ofta. Det är lättare att felsöka om du testar din kod ofta.
- Läs felmeddelanden. De kan ge dig en hint om vad som är fel.
- Använd versionhantering för att spara ditt arbete. Det kan vara bra att gå tillbaka till en tidigare version om du råkar förstöra något.
- Ha roligt! Programmering är kul och det är en bra känsla när du lyckas lösa en uppgift.
- Koppla av och koppla på frontalloben. Ibland kan det hjälpa att ta ett djupt andetag och släppa fokus från problemet för att sedan låta lösningen kommer till dig.
- Ta en paus om du känner dig frustrerad. Ibland kan det hjälpa att ta en paus och komma tillbaka senare.
- Ha tålamod. Det kan ta tid att lösa problemen. Ge inte upp!


Fler övningar online hittar du på:
- [FutureSkill](https://futureskill.com/).
- [LeetCode](https://leetcode.com/problemset/all/).
- [Advent of Code](https://adventofcode.com/). <-- Julkalender för programmerare.
- [CodeSignal](https://app.codesignal.com/).
- [HackerRank](https://www.hackerrank.com/domains/tutorials/10-days-of-javascript).
- [Exercism](https://exercism.io/my/tracks).
- [Codecademy](https://www.codecademy.com/learn).
- [edabit](https://edabit.com/challenges/python3).
- [Codewars](https://www.codewars.com/).
- [Project Euler](https://projecteuler.net/).
- [Daily Coding Problem](https://www.dailycodingproblem.com/).
- [Codeforces](https://codeforces.com/).



