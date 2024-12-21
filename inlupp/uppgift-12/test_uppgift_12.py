from uppgift_12 import create_student_register

def test_create_student_register():
    students = [("Anna", 20), ("Bertil", 25), ("Cecilia", 22)]
    assert create_student_register(students) == {"Anna": 20, "Bertil": 25, "Cecilia": 22}


