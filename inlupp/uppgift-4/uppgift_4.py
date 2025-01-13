# Uppgift 4
# Skapa en funktion fibonacci(n) som returnerar en lista med de första n Fibonacci-talen.

def fibonacci(n: int) -> list:
    """
    Fibonacci(n) som returnerar en lista med de första n Fibonacci-talen.
    """
    if n == 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        # Isolera dem första 2 talen
        return [0, 1]
    else:
        fib_sequence = [0, 1]
        # index         0, 1
        # Om vi vill ha dem 5 första talen:
        # 
        # talen [0, 1, 1, 2, 3]
        # index [0, 1, 2, 3, 4]
        for i in range(2, n):
            print(f"index är: {i}")
            fib_sequence.append(
                fib_sequence[i - 2] + fib_sequence[i - 1]
                )
        # Utanför for-loop:
        return fib_sequence

# Om vi skickar in 10
# Fibonacci: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
# index:     [0, 1, 2, 3, 4, 5, 6,  7,  8,  9] = 10st tal
# varv 1 och två, hoppar vi över
# varv 3: vi kollar index 3 - 2 och 3 - 1, alltså index 1 och 2
# och plussar ihop
# När index är 4, kollar vi tal 4-2 och 4-1, alltså index 2 och 3
# När index är 5, kollar vi tal 5-2 och 5-1, alltså index 3 och 4
# När index är 6, kollar vi tal 6-2 och 6-1, alltså index 4 och 5
# När index är 7, kollar vi tal 7-2 och 7-1, alltså index 5 och 6 (5+8=13)
# När index är 8, kollar vi tal 8-2 och 8-1, alltså index 6 och 7 (8+13=21)
# När index är 9, kollar vi tal 9-2 och 9-1, alltså index 7 och 8 (13+21=34)

# [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
# [1, 2, 3, 4, 5, 6, 7,  8,  9, 10]

print(fibonacci(3))
print(fibonacci(5))
print(fibonacci(10))
