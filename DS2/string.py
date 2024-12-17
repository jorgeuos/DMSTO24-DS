
print("Hej" * 3)

text = "DataScience"

print(text[0])

print(text[-1])

print(text[0],text[1])

print(text[0:5])

text = " Python är roligt "

no_whitespace = text.strip()

print(no_whitespace)

fantastico = no_whitespace.replace("roligt", "fantastiskt")

print(fantastico)

UPPER = fantastico.upper()

print(UPPER)


name = input("Vad heter du? ")
age = input("Hur gammal är du? ")

print(f"Hej, {name}! Du är {age} år ung.")

