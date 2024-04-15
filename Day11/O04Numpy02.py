
import  numpy as np

arr = np.array([1, 2, 3, 4, 5])
print(f"arr :{arr}")

print("-" * 60)
print(f"arr[0] :{arr[0]}")
print(f"arr[3] :{arr[3]}")
print(f"arr[1] + arr[3] = {arr[1] + arr[3]}")

print("-" * 60)
arr1 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(f"arr1 :\n{arr1}")

print(f"arr1[0, 1] :{arr1[0, 1]}")
print(f"arr1[1, 4] :{arr1[1, 4]}")

print("-" * 60)
arr2 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [11, 12, 13]]])
print(f"arr2 :\n{arr2}")

print(f"arr2[0, 1, 2] :{arr2[0, 1, 2]}")
print(f"arr2[1, 1, 1] :{arr2[1, 1, 1]}")

print("Slicing".center(60, "-"))

arr1  = np.array([1, 2, 3, 4, 5, 6, 7])

print(f"arr1 :{arr1}")

print(f"arr1[1:5] :{arr1[1:5]}")

print(f"arr1[4:]  :{arr1[4:]}")

print(f"arr1[-3:-1] :{arr1[-3:-1]}")

print(f"arr1[1:5:2] :{arr1[1:5:2]}")
print(f"arr1[::2] :{arr1[::2]}")

print("-" * 60)

arr2 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(f"arr2 :\n{arr2}")

print(f"arr2[0:2, 2] :{arr2[0:2, 2]}")
print(f"arr2[0:2, 1:4]:\n{arr2[0:2, 1:4]}")
