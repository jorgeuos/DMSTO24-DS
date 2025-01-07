
def is_even(number: int) -> bool:
    """
    Returnerar True om talet är jämnt, annars False.
    """
    trueOrFalse = (number % 2 == 0)
    return trueOrFalse
    
print(is_even(2))
print(is_even(3))
print(is_even(4))
print(is_even(5))
print(is_even(6))

