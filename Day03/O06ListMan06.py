"""
sort    - sort will sort the original array
sorted  - sorted will take a copy of the array sorts it and returns it

"""

print("sort".center(60, "-"))
l1 = [7, 10, 1, 6, 9, 2, 4, 3, 8, 5]
print(f"l1 :{l1}")

res_asc = sorted(l1)
print(f"Ascending order :{res_asc}")

l1.sort(reverse=True)
print(f"Descending Order :{l1}")

print("-" * 60)
l1 = [7,'zebra', 10, 'apple', 1, 'yellow', 6, 'blue', 9, 'white', 2, 'green', 4, 'xray', 3, 'pink', 8, 'violet', 5, 'dog', 'cat', 'elephant', 1024, 183, 29, 265, 2112]

print(f"l1 :{l1}")

print("-" * 60)
res = sorted(l1, key=ascii)
print(f"res :{res}")

# for i in res:
#     i = str(i)
#     if i.isnumeric():
#         print(res.index(int(i)))
#         break

print(res[:12] + sorted(res[12:]))
print("-" * 60)

cities = ['vishakapatnam', 'mysore', 'delhi', 'thiruvananthapuram', 'bangalore', 'chennai', 'ooty', 'hyderabad', 'pune', 'mumbai']
print(f"cites :{cities}")

print("-" * 60)
res_asc = sorted(cities, key=len)
print(f"Ascending  :{res_asc}")

print("-" * 60)
res_desc = sorted(cities, key=len, reverse=True)
print(f"Descending :{res_desc}")

print("reversed".center(60, "-"))
l1 = [7, 10, 1, 6, 9, 2, 4, 3, 8, 5]
print(f"l1 :{l1}")

res = list(reversed(l1))
print(f"res :{res}")
