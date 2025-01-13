
def fibonacci(n, iteration):
   print(f"Iteration: {iteration}, n är: {n}")
   iteration += 1
   if n <= 1:
       return n
   return fibonacci(n - 1, iteration) + fibonacci(n - 2, iteration)

print(fibonacci(6, 1))  # Output: 8


# Skickar in siffra i fibonacci 6
# n är 6
# 6-1
# som anropar fibonnaci med 5
# n är 5
# 5-1
# som anropar fibonacci med 4
# n är 4
# som anropar fibonacci med 3
# n är 3
# 3-1
# som anropar fibonacci med 2
# n är 2



def fibonacci(n, listan):
    fib = []
    if n <= 1:
        fib.append(0)
        fib.append(1)
        return fib
    sequence = fibonacci(n - 1) + fibonacci(n - 2)
    print()
    fib.append(sequence)
    return fib

# print(fibonacci(6))  # Output: 8


# Iteration: 1, n är: 6
# Iteration: 2, n är: 5
# Iteration: 3, n är: 4
# Iteration: 4, n är: 3
# Iteration: 5, n är: 2
# Iteration: 6, n är: 1
# Iteration: 6, n är: 0
# Iteration: 5, n är: 1
# Iteration: 4, n är: 2
# Iteration: 5, n är: 1
# Iteration: 5, n är: 0
# Iteration: 3, n är: 3
# Iteration: 4, n är: 2
# Iteration: 5, n är: 1
# Iteration: 5, n är: 0
# Iteration: 4, n är: 1
# Iteration: 2, n är: 4
# Iteration: 3, n är: 3
# Iteration: 4, n är: 2
# Iteration: 5, n är: 1
# Iteration: 5, n är: 0
# Iteration: 4, n är: 1
# Iteration: 3, n är: 2
# Iteration: 4, n är: 1
# Iteration: 4, n är: 0
