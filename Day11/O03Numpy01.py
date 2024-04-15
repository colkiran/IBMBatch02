import numpy as np

arr = np.array([1, 2, 3, 4, 5])

print(f"arr :{arr}")

print(type(arr))

print(f"Version :{np.__version__}")

print("Zero Dimension".center(60, "-"))
arr0 = np.array(100)
print(f"arr0 :{arr0}")

print(f"arr0.ndim :{arr0.ndim}")

print("One Dimension".center(60, "-"))
arr1 = np.array([1, 2, 3, 4, 5])
print(f"arr1 :{arr1}")
print(f"arr1.ndim :{arr1.ndim}")

print("Two Dimension".center(60, "-"))
arr2 = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(f"arr2 :\n{arr2}")
print(f"Dimension :{arr2.ndim}")

print("Three Dimension".center(60, "-"))
arr3 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9],[10, 11, 12]]])
print(f"arr3 :\n{arr3}")
print(f"Dimension :{arr3.ndim}")
