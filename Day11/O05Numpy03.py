
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
print(f"arr :{arr}")
print(arr.reshape(4, 3))

print("-" * 60)

print(arr.reshape(2, 6))

print("-" * 60)

print(arr.reshape(3, 4))

print("-" * 60)

print(arr.reshape(2, 3, 2))

print("-" * 60)

arr1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(f"arr1 :{arr1}")
newarr= arr1.reshape(3, 3)
print(newarr)

print("-" * 60)
arr3 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(f"arr3 :\n{arr3}")

print("-" * 60)
# iterating
for x in arr3:
    print(x)

print("-" * 60)
for x in arr3:
    for y in x:
        for z in y:
            print(z)

print("-" * 60)

arr4 = np.array([[[1, 2], [3, 4]], [[5, 6],[7, 8]]])
print(f"arr4 :\n{arr4}")

for x in np.nditer(arr4):
    print(x)
