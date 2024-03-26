
"""
1. arithmetic operators
2. augmentor operator
"""

print("Comparison Operator".center(60, "-"))
# ==, !=, >, >=, <, <=

print(f"1 == 1 :{1 == 1}")
print(f"1 == 2 :{1 == 2}")
print("-" * 60)

a = 10
b = 8
print(f"a :{a}\tb :{b}")
print(f"a > b :{a > b}")
print(f"a < b :{a < b}")
print(f"a == b :{a == b}")

print("Logical Operators".center(60, "-"))
# and, or, not
print(f"1 == 1 and 1 == 1 :{1 == 1 and 1 == 1}")
print(f"1 == 1 and 1 == 2 :{1 == 1 and 1 == 2}")

print("-" * 60)
print(f"1 == 1 or 1 == 1 :{1 == 1 or 1 == 1}")
print(f"1 == 1 or 1 == 2 :{1 == 1 or 1 == 2}")

print("-" * 60)
print(f"not(1 == 1 or 1 == 1) :{not(1 == 1 or 1 == 1)}")
print(f"not(1 == 1 or 1 == 2) :{not(1 == 1 or 1 == 2)}")

print("-" * 60)
print(f"a :{ord('a')}")     # integer representation of unicode characters
print(f"z :{ord('z')}")
print(f"A :{ord('A')}")
print(f"Z :{ord('Z')}")

print(f'"apple" > "orange" :{"apple" > "orange"}')       # compares the string using ascii values
print(f'"orange" > "apple" :{"orange" > "apple"}')


print("Bitwise Operators".center(60, "-"))
# binary values

print(f"5 | 3 :{5 | 3}")
print(f"5 & 3 :{5 & 3}")
print(f"5 ^ 3 :{5 ^ 3}")
print(f"5 << 1 :{5 << 1}")
print(f"8 << 1 :{8 << 1}")
print(f"5 << 2 :{5 << 2}")
print(f"16 >> 1 :{16 >> 1}")
print(f"5 >> 1 :{5 >> 1}")

print("Ternary Operator".center(60, "-"))
a = 18
print("Eligible" if a >= 18 else "Not Eligible")
