
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
print(y)


