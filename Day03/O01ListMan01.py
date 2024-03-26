
l1 = list()
print(f"l1 :{l1}")
print(type(l1))

print("-" * 60)
l2 = [1, 2, 3, 4.1, 5.2, 6.7, 8+2j, 9-3j, 'ten', 'eleven', 'twelve', True, False]
print(f"l2 :{l2}")
print(type(l1))

print("-" * 60)
l3 = list(range(1, 11))
print(f"l3 :{l3}")
print(type(l3))

print("-" * 60)
values = range(10, 40, 10)
print(f"values :{values}")

# unpack the list
a, b, c = values        # 10, 20, 30
print(f"a :{a}, b :{b}, c :{c}")

print("-" * 60)
values = list(range(10, 101, 10))
print(f"values :{values}")

a, b, *c = values       # varaible with * can accept more than one value
print(f"a :{a}, b :{b}, c :{c}")

print("-" * 60)
a, *b, c = values
print(f"a :{a}, b :{b}, c :{c}")

print("-" * 60)
*a, b, c = values
print(f"a :{a}, b :{b}, c :{c}")

print("-" * 60)
lst1 = [1, 2, 3]
lst2 = [4, 5, 6]

lst3 = [lst1, lst2]
print(f"lst3 :{lst3}")
print(len(lst3))

print("-" * 60)
lst4 = [*lst1, *lst2]
print(f"lst4 :{lst4}")
print(len(lst4))

