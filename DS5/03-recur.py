
def factorial(n):
   print(f"n = {n}")
   if n == 1:  # Basfall
       return 1
   result = n * factorial(n - 1)  # Rekursivt fall
   print(result)
   return result

print(factorial(10))  # Output: 120

