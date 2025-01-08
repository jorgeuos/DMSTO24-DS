
# def greet(name):
#    return f"Hej, {name}!"

# greeter = greet("Anna")
# print(greeter)
# print(greet("Jonas"))
# print(greet("Maria"))
# print(greet("Peter"))

# print(f"Hej, {greeter}!")

def greet(name, greeting="Hej"):
   return f"{greeting}, {name}!"

print(greet("Anna"))  # Output: Hej, Anna!
print(greet("Anna", "Hello"))  # Output: Hello, Anna!


