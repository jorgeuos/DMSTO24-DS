# Uppgift 2
# Skapa en funktion sum_list(numbers) som returnerar summan av alla siffror i listan.

def sum_list(numbers: list) -> int:
    """
    Jag returnerar summan av alla siffror i listan.
    """
    summan = 0
    for num in numbers:
        summan = summan + num
    return summan

print(sum_list([-1, -2, -3]))
# sum_list([1, 2, 3])
