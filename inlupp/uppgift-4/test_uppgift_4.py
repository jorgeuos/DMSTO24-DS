from uppgift_4 import fibonacci

def test_fibonacci():
    assert fibonacci(5) == [0, 1, 1, 2, 3]
    assert fibonacci(0) == []
    assert fibonacci(1) == [0]


