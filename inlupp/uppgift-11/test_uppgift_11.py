from uppgift_11 import word_count

def test_word_count():
    assert word_count("hello world") == 2
    assert word_count("") == 0
    assert word_count("Python är fantastiskt!") == 3


