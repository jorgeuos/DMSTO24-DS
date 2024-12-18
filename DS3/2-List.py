
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
# print(reallyLongList.reverse())


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