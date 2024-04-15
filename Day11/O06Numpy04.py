
import numpy as np
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.vstack((arr1, arr2))
print(f"arr :\n{arr}")

print("-" * 60)
arr3 = np.hstack((arr1, arr2))
print(f"arr3 :\n{arr3}")
