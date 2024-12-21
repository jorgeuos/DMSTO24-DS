from uppgift_5 import filter_odd

def test_funktion():
    assert filter_odd([1, 2, 3, 4]) == [2, 4]
    assert filter_odd([1, 3, 5]) == []
    assert filter_odd([]) == []


