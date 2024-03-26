
print("pop".center(60, "-"))
l1 = list(range(1, 11))
print(f"l1 :{l1}")

res = l1.pop(7)
print(f"res :{res}")

res = l1.pop(3)
print(f"res :{res}")

res = l1.pop()
print(f"res :{res}")

print("remove".center(60,"-"))
# remove will work on values
l1 = [1, 2, 1, 1, 1, 1, 2, 3, 2, 2, 2, 2, 1, 1, 1, 1, 2, 3, 1, 1, 1, 2, 2, 2, 2, 3, 2, 1, 1, 1, 1, 1, 2, 2, 2]
print(f"l1 :{l1}")

print("-" * 60)
l1.remove(3)    # removes the first occurance of 3 from LHS
print(f"l1 :{l1}")

l1.remove(3)
print(f"l1 :{l1}")

l1.remove(3)
print(f"l1 :{l1}")

print("clear".center(60, "-"))
l1 = list(range(1, 11))
print(f"l1 :{l1}")

l1.clear()
print(f"l1 :{l1}")      # results to an empty list

print("count".center(60, "-"))

l1 = [1, 2, 1, 1, 1, 1, 2, 3, 2, 2, 2, 2, 1, 1, 1, 1, 2, 3, 1, 1, 1, 2, 2, 2, 2, 3, 2, 1, 1, 1, 1, 1, 2, 2, 2]
print(f"l1 :{l1}")

print("-" * 60)
print(f"1 :{l1.count(1)}")
print(f"2 :{l1.count(2)}")
print(f"3 :{l1.count(3)}")
print(f"5 :{l1.count(5)}")

print("index".center(60, "-"))

print(f"l1 :{l1}")

print("-" * 60)

print(f"first occurance of 3 :{l1.index(3)}")
print(f"second occurance of 3 :{l1.index(3,l1.index(3) + 1)}")
print(f"third occurance of 3 :{l1.index(3, l1.index(3,l1.index(3) + 1) + 1)}")
