from uppgift_2 import sum_list

def test_sum_list():
    assert sum_list([1, 2, 3]) == 6
    assert sum_list([]) == 0
    assert sum_list([-1, -1, 2]) == 0
    assert sum_list([1, 2, 3, 4, 5, 6]) == 21


