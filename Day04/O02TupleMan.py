
t1 = tuple()
print(f"t1 :{t1}")
print(type(t1))

print("-" * 60)
t2 = (1, 2, 3, 4.5, 5.1, 6.3, 7 + 0j, 8 - 1j, 'nine', 'ten', 'eleven', True, False )
print(f"t2 :{t2}")
print(type(t2))

print("-" * 60)
t3 = tuple(range(1, 11))
print(f"t3 :{t3}")
print(type(t3))

print("-" * 60)

# 'count', 'index'

t4 = (1, 2, 2, 2, 1, 2, 3, 1, 1, 2, 1, 2, 1, 2, 1, 2, 3, 1,2, 2,2,1, 1,1, 1, 2, 1, 2, 2, 3, 1, 2, 1, 2, 1, 2, 1, 2, 2, 2)
print(f"t4 :{t4}")

print(f"1 :{t4.count(1)}")
print(f"2 :{t4.count(2)}")
print(f"3 :{t4.count(3)}")
print(f"5 :{t4.count(5)}")

print("index".center(60, "-"))
print(f"t4 :{t4}")
print(f"First 3 :{t4.index(3)}")
print(f"Second 3 :{t4.index(3, t4.index(3) + 1)}")
print(f"First 3 :{t4.index(3, t4.index(3, t4.index(3) + 1)+1)}")

print("-" * 60)
t5 = tuple(range(1, 11))
print(f"t5 :{t5}")
print(type(t5))

l1 = list(t5)
print(f"l1 :{l1}")
l1.extend(list(range(11, 16)))
print(f"l1 :{l1}")

t5 = tuple(l1)
print(f"t5 :{t5}")
print(type(t5))
