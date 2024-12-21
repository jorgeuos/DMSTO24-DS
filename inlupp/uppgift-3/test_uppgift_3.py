from uppgift_3 import max_in_list

def test_max_in_list():
    assert max_in_list([1, 2, 3]) == 3
    assert max_in_list([-5, 0, 5]) == 5
    assert max_in_list([10]) == 10

