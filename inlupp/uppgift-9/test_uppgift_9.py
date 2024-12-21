from uppgift_9 import is_palindrome

def test_is_palindrome():
    assert is_palindrome("radar") == True
    assert is_palindrome("python") == False
    assert is_palindrome("") == True


