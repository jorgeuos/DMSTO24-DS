



# x = int(input("Skriv ett tal: "))
# if x > 0:
#    print("Talet är positivt")
# elif x < 0:
#    print("Talet är negativt")
# else:
#    print("Talet är noll")



# while True:
#    x = int(input("Skriv ett tal: "))
#    if x > 0:
#       print("Talet är positivt")
#    elif x < 0:
#       print("Talet är negativt")
#    else:
#       print("Talet är noll")
#    fortsatt = input("Vill du fortsätta? (j/n): ")
#    if fortsatt == "n":
#       print("Hej då!")
#       break

# Gör med While-loop istället

# x = input("Skriv ett tal: ")
# while x != "exit" and x != "x":
#     x = int(x)
#     if x > 0:
#         print("Talet är positivt")
#     elif x < 0:
#         print("Talet är negativt")
#     else:
#         print("Talet är noll")
#     x = input("Skriv ett tal: ")

# x = 1
# print(type(x) == int)

x = input("Skriv ett tal: ")
y = 0
while ( type(x) == int or y == 0):
    x = int(x)
    if x > 0:
        print("Talet är positivt")
    elif x < 0:
        print("Talet är negativt")
    else:
        print("Talet är noll")
    y += 1
    x = input("Skriv ett tal: ")
    try:
        x = int(x)
    except ValueError:
      print("Du skrev inte ett tal, hej då!")
      continue












password = ""
while password != "hemligt":
   password = input("Ange lösenord: ")
print("Rätt lösenord!")


# Skapa ett program som kollar om ett tal är jämnt eller udda.
x = 10
if x % 2 == 0:
    print(f'{x} är ett jämnt tal.')
else:
    print(f'{x} är ett udda tal.')




# Skapa en loop som skriver ut alla siffror mellan 1 och 10.
for i in range(1, 11):
    print(i)

# Skapa en while-loop som räknar ned från 10 till 1 och skriver "Starta!" när den är klar.
i = 10

while i > 0:
    print(i)
    i -= 1

print("Starta!")

# Eller

i = 10
while i > 0:
    print(i)
    i -= 1
else:
    print("Starta!")


