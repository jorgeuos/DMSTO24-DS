from uppgift_1 import is_odd

def test_is_odd():
    assert is_odd(1) == True
    assert is_odd(2) == False
    assert is_odd(3) == True
    assert is_odd(0) == False
    assert is_odd(-2) == False
    assert is_odd(-1) == True



