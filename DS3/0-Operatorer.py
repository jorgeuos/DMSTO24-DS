x = 10
y = 5

print(x > 5 and y < 10)  # Output: True
print(x > 5 or y < 10)  # Output: 
print(x > 5 and y < 4)  # Output: 
print(x > 5 or y < 4)  # Output:

z = 3

print(x > 5 or y < 4 and z == 3)  # Output:
print(x > 5 or y < 4 and z != 3)  # Output:

print(x > 15 or y < 4 and z != 3)  # Output:


print(x > 5 and y < 5 and z == 3)  # Output:

# Överkurs
print(x > 5 and y <= 5 and z == 3)  # Output:
