

with open("data.txt", "w") as file:
   file.write("Name, Age, City\nAnna, 25, Stockholm\n")
   file.write("Björn, 30, Göteborg\n")
   file.append

with open("data.txt", "r") as file:
   print(file.read())

with open("data.txt", "a") as file:
   file.write("Björn, 30, Göteborg\n")

with open("data.txt", "r") as file:
   print(file.read())
