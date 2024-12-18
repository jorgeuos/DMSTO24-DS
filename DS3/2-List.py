
my_list = ["a", "b", "c", "d"]
print(my_list[0])  # Output: a

print(my_list[-2])

# Lista med heltal
numbers = [1, 2, 3, 4, 5]

# Tom lista
empty_list = []
print(empty_list)

print(type(empty_list))

if empty_list == "[]":
    print("Listan är tom 1")

if empty_list == []:
    print(empty_list == [])
    print("Listan är tom 2")

if empty_list:
    print("Listan är tom 3")

if not empty_list:
    print("Listan är tom 4")

listaMedEttElement = [1]

if listaMedEttElement:
    print("Listan är inte tom 5")

if not listaMedEttElement:
    print("Listan är tom 6")

listaMedFlera = [1,2,4]

if listaMedFlera:
    print("Listan är inte tom 7")

# Blandade datatyper
mixed_list = [1, "text", True]

print(mixed_list[0])
print(mixed_list[1])
print(mixed_list[2])

print(mixed_list)

longList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(longList[0:5])

reallyLongList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

print(reallyLongList[0:])
print(reallyLongList[4:])
print(reallyLongList[:14])
print(reallyLongList[3:14])
print(reallyLongList[-1:0])

reallyLongList.reverse()

print(reallyLongList)


my_list = ["äpple", "banan", "körsbär"]

for fruit in my_list:
    if fruit != "körsbär":
      print("Jag gillar " + fruit)
    else:
      print("Jag gillar inte " + fruit)



reallyLongList = ["äpple", "banan", "körsbär", "druva", "apelsin", "päron", "kiwi", "mango", "passionsfrukt", "ananas"]

for index, number in enumerate(reallyLongList):
    print(index, number)

reallyLongList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

for number in reallyLongList:
    if number % 2 == 0:
        print(number)

for number in reallyLongList:
    if number % 2 != 0:
        print(number)


# Reverse

my_list = ["äpple", "banan", "körsbär"]

my_list.reverse()
print(my_list)

reallyLongList = ["äpple", "banan", "körsbär", "druva", "apelsin", "päron", "kiwi", "mango", "passionsfrukt", "ananas"]

print("Length: ")
print(len(reallyLongList))

x = 1
for i, fruit in enumerate(reallyLongList):
    if i == (i+1):
        continue
    if (i+1) % 3 == 0:
        print(fruit)
    # x += 1
    x = x + 1
    # Funkar inte
    # x++

print(type(x))
print("x är:")
print(x)

# Unset variable
x = None

print(my_list)
my_list[1] = "blåbär"
print(my_list)

my_list.insert(1, "orange")
print(my_list)

my_list.append("jordgubbe")
my_list.append("blåbär")
my_list.append("blåbär")
my_list.append("blåbär")
my_list.append("Blåbär")
my_list.append("BlåBär")

# Funkar inte
# my_list.prepend("hallon")

# Bygger en egen prepend-funktion
def prepend(prependList, value):
    prependList.insert(0, value)

prepend(my_list, "hallon")

print(my_list)

try:
    my_list.remove("blåbär")
    my_list.remove("blåbär")
    my_list.remove("blåbär")
    my_list.remove("blåbär")
    my_list.remove("blåbär")
    my_list.remove("blåbär")
    my_list.remove("blåbär")
    my_list.remove("blåbär")
except ValueError:
    print("Det gick inte att ta bort blåbär")

print(my_list)

my_list.pop()

print(my_list)
