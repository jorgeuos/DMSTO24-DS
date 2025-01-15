"""
Några kommandon för att göra det enklare med filhantering.
"""
import os

# Vart är jag någonstans?
iAmHere = os.getcwd()

print("os.getcwd()")
print(iAmHere)

with open(iAmHere + "/ovningar/test-fil.txt","w") as file:
    file.write(iAmHere)


