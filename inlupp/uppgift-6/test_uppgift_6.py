from uppgift_6 import multiplication_table

def test_funktion():
    assert multiplication_table(2, 3) == [2, 4, 6]
    assert multiplication_table(3, 5) == [3, 6, 9, 12, 15]


