
# CRUD
# create
l1 = list(range(1, 11))

# read
print(f"l1 :{l1}")
print(f"l1[0] :{l1[0]}")
print(f"l1[3] :{l1[3]}")
print(f"l1[-1] :{l1[-1]}")


print("-" * 60)
for i in l1:
    print(i, end=" ")
print()

print("-" * 60)
# update or add
print(f"l1 :{l1}")
# insert elements into the list it gets replaced - lists are static
l1[5] = 250
l1[7] = 300
print(f"l1 :{l1}")

print("-" * 60)
# delete

del l1[5]
del l1[6]
print(f"l1 :{l1}")

# print("-" * 60)
# print(dir(l1))
print("append".center(60, "-"))
l1 = list(range(1, 6))
print(f"l1 :{l1}")

l1.append(6)
l1.append(7)
l1.append(8)
l1.append(9)

print(f"l1 :{l1}")
l1.append([10, 11, 12, 13, 14])
print(f"l1 :{l1}")

# print - 11, 12, 13
print(f"l1[9][1:4] :{l1[9][1:4]}")

print("extend".center(60, "-"))
l2 = [6, 7, 8, 9, 10]
print(F"l2 :{l2}")

l2.extend([11, 12, 13, 14, 15])
print(f"l2 :{l2}")

print("insert".center(60, "-"))
l3 = [1, 2, 3, 4, 5]
print(f"l3 :{l3}")

l3.insert(1, 1.5)
l3.insert(3, 2.5)
l3.insert(5, 3.5)
l3.insert(7, 4.5)

print(f"l3 :{l3}")

l3.insert(20, 100)
print(f"l3 :{l3}")
print(len(l3))

