
print(sum([x ** 2 for x in range(1, 11)]))       # list comprehension

print(sum((x ** 2 for x in range(1, 11))))

print("-" * 60)

from sys import getsizeof
val1  = [x ** 2 for x in range(10000)]
print(f"Comprehesion size of list :{getsizeof(val1)}")
val2 = (x ** 2 for x in range(10000))
print(f"Generator size of list :{getsizeof(val2)}")

val3 = (x for x in range(10))

for num in val3:
    print(num, end=" ")
print()

