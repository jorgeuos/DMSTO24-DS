def divide_numbers(a, b):
   quotient = a // b
   remainder = a % b
   return quotient, remainder

q, r = divide_numbers(10, 3)
print(f"Kvot: {q}, Rest: {r}")  # Output: Kvot: 3, Rest: 1

def greet(name, greeting):
   return f"{greeting}, {name}!"

print(greet("Anna", "Hej"))  # Output: Hej, Anna!
print(greet(greeting="Hello", name="Anna"))  # Output: Hello, Anna!


