from uppgift_7 import validate_password

def test_funktion():
    assert validate_password("abc12345") == True
    assert validate_password("short") == False
    assert validate_password("password1") == True


