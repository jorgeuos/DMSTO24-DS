
try:
   x = int("hej")  # Försöker konvertera en sträng till heltal
except:
   print("Ett fel uppstod.")


try:
    x = int("123")  # Försöker konvertera en sträng till heltal
    print(x)
except:
   print("Ett fel uppstod 2.")


print("Programmet fortsätter här.")  # Denna rad körs oavsett om det uppstod ett fel eller inte


try:
    y = int("tre")  # Försöker konvertera en sträng till heltal
    print(y)
except:
   print("Ett fel uppstod 3.")

# Bör generera ett fel
# print(y)

print("Fånga specifika fel")

try:
   x = int("hej")
except ValueError:
   print("Ett värdefel uppstod.")

# Vi kan hanter flera olika fel
try:
    x = int("hej")
    y = 0
    print(x / y)
except ZeroDivisionError:
    print("Ett ZeroDivisionError fel uppstod.")
except ValueError:
   print("Ett värdefel uppstod.")


try:
    x = int("123")
    y = 0
    print(x / y)
except ZeroDivisionError:
    print("Ett ZeroDivisionError fel uppstod.")
except ValueError:
   print("Ett värdefel uppstod.")

try:
   x = 10 / 0
except ZeroDivisionError:
   print("Du kan inte dela med 0.")
finally:
   print("Programmet fortsätter.")

# Bör ge syntaxfel
# x = 10 / 0

# Kommer inte att nå hit ner
print("Men jag vill ju fortsätta")


print("Nu är vi klara.")

"""
Work in progress
def delaMedFunction(tal):
    try:
        print(f"10 / {tal}")
        x = 10 / tal
        print(f"10 / {tal} = {x}")
    except ZeroDivisionError:
        print("Du kan inte dela med 0.")
        # Kör någon annan kod här
        # Hantera felet
        return  False
    except:
        print("Vi fick ett fel.")
    finally:
        print("Försök igen.")
        z = input("Skriv in ett tal att dela med: ")
        delaMedFunction(z)

q = input("Skriv in ett tal att dela med: ")
delaMedFunction(q)
"""