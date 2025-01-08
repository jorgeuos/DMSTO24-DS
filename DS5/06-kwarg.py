# Skapa en funktion som tar emot:
# En lista av tal.
# Ett nyckelord som anger operation (add, multiply).
# Extra parametrar för operationens detaljer.


def calculate(numbers, operation, **kwargs):
    sum = 0
    if "start" in kwargs:
       sum = kwargs["start"]
    # print(sum)
    for num in numbers:
      if operation == "add":
        sum = sum + num
      elif operation == "multiply":
        sum *= num
    return sum

value = calculate([1, 2, 3], "add", start=10)
print(value)
value = calculate([1, 2, 3], "multiply", start=10)
print(value)
