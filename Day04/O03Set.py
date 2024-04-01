
s1 = set()
print(f"s1 :{s1}")
print(type(s1))
print("-" * 60)

s2 = {1, 2, 3, 4.5, 5.2, 6.9, 'seven', 'eight', 'nine', 10+0j, 11-3j, True, False}
print(f"s2 :{s2}")
print(type(s2))

print("-" * 60)
s3 = set(range(1, 11))
print(f"s3 :{s3}")
print(type(s3))

print("-" * 60)
s1 = {1, 2, 3}
print(f"s1 :{s1}")
# print(dir(s1))

print("add".center(60, "-"))
print(f"s1 :{s1}")

s1.add(4)
s1.add(1)
s1.add(5)
s1.add(2)
s1.add(3)
s1.add(6)

print(f"s1 :{s1}")

print("update".center(60, "-"))
print(f"s1 :{s1}")

s1.update([1, 2, 3])
s1.update([5, 6, 7])
s1.update([4, 5, 6])
s1.update([1, 5, 7])
s1.update([8, 9, 10])
s1.update([2, 3, 4])

print(f"s1 :{s1}")

# pop, remove, discard
print("pop".center(60, "-"))
print(f"s1 :{s1}")

res = s1.pop()
print(f"res :{res}")

res = s1.pop()
print(f"res :{res}")

print(f"s1 :{s1}")

print("remove".center(60, "-"))
print(f"s1 :{s1}")
s1.remove(4)
s1.remove(8)

# s1.remove(1)
print(f"s1 :{s1}")

print("discard".center(60, "-"))
print(f"s1 :{s1}")
s1.discard(6)
s1.discard(10)

s1.discard(1)
print(f's1 :{s1}')

print("-" * 60)
A = {1, 2, 3, 4, 5, 6}
print(f"A :{A}")
print(type(A))

B = {5, 6, 7, 8, 9, 10}
print(f"B :{B}")
print(type(B))

print("union".center(60, "-"))
print(f"A union B :{A | B}")
print(f"B union A :{B.union(A)}")

print("Intersection".center(60, "-"))
print(f"A intersection B :{A & B}")
print(f"B intersection A :{B.intersection(A)}")

print("difference".center(60, "-"))
print(f"A difference B :{A - B}")
print(f"B difference A :{B.difference(A)}")

print("symmetric difference".center(60, "-"))
print(f"A symmetric difference B :{A ^ B}")
print(f"B symmetric difference A :{B.symmetric_difference(A)}")

print("frozen set".center(60, "-"))
fs = frozenset([1, 2, 3, 4, 5])
print(f"fs :{fs}")
print(type(fs))
# they are immutable
