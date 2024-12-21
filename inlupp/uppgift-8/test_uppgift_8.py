from uppgift_8 import count_letters

def test_funktion():
    assert count_letters("hello") == {"h": 1, "e": 1, "l": 2, "o": 1}
    assert count_letters("") == {}
    assert count_letters("aaa") == {"a": 3}


