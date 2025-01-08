
with open("personer-1.txt", "w") as file:
   file.write("Name, Age, City\nAnna, 25, Stockholm\n")
   file.write("Björn, 30, Göteborg\n")


with open("personer-2.txt", "w") as file:
   file.write("Name, Age, City\nMaria, 27, Stockholm\n")

filenames = ["personer-1.txt", "personer-2.txt"]

def combine_files(filenames: list[str]):
    with open("kombinerad-personer.txt", "w") as combined_file:
        for index, filename in enumerate(filenames):
            with open(filename, "r") as individual_file:
                for i, line in enumerate(individual_file):
                    if index == 0 and i == 0:
                        combined_file.write(line)
                    elif index != 0 and i == 0:
                        continue
                    else:
                        combined_file.write(line)

combine_files(filenames)

# print(index)

# import os
# os.remove("example.txt")

