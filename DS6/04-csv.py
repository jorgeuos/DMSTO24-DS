import csv

with open("data.csv", "r") as file:
   reader = csv.reader(file)
   for row in reader:
       print(row)

# import csv

# with open("data.csv", "r") as file:
#    reader = csv.DictReader(file)
#    for row in reader:
#        print(row)
#     #    print(row.get("Name"))

# data = [
#    ["Name", "Age", "City"],
#    ["Anna", 25, "Stockholm"],
#    ["Björn", 30, "Göteborg"]
# ]
# with open("output.csv", "w", newline="") as file:
#    writer = csv.writer(file)
#    writer.writerows(data)

# data = [
#    {"Name": "Anna", "Age": 25, "City": "Stockholm"},
#    {"Name": "Björn", "Age": 30, "City": "Göteborg"}
# ]
# with open("output-1.csv", "w", newline="") as file:
#    writer = csv.DictWriter(file, fieldnames=["Name", "Age", "City"])
#    writer.writeheader()
#    writer.writerows(data)


with open("data_semicolon.csv", "r") as file:
   reader = csv.reader(file, delimiter=";")
   for row in reader:
       print(row)


