# Fortsättning txt filer


# lista = ["Maria","Jose"] # Vanlig lista
# listaMedIndex = [
#     0: "Maria",
#     1: "Jose"
# ]

# with open("data.txt", "r") as file:
#     print(file.read())
#     for i, line in enumerate(file):
#         print(f"Rad: {i}: {line.strip()}")

# with open("data.txt", "r") as file:
#     count = 0
#     for i, line in enumerate(file):
#         count += 1
#     print(count)

# Vi ska leta efter nyckelordet "Anna"
keyword = "Björn"
# Vi öppnar vår data.txt fil, i läs-läge
with open("data.txt", "r") as file:
    # Vi loopar igenom alla rader i filen
    for line in file:
        # Vi kollar om vårt nyckelord existerar per rad
        if keyword in line:
            # Om vi matchar, så skriv ut resultat:
            print(line.strip())
        else:
            print(f"Ingen {keyword}")
