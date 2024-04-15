
import pandas as pd
import numpy as np

arr = np.array([1, 2, 3, 4, 5])
print(f"arr :{arr}")
psrs = pd.Series(arr)
print(f"Pandas Series :\n{psrs}")

print("-" * 60)

psrs1 = pd.Series([1, 2, 3], index=['a', 'b', 'c'])
print(f"Pandas Series :\n{psrs1}")

print("-" * 60)

a = pd.Series(['Java', 'C', 'C++', np.NAN])
print(a)
print(a.map({'Java': 'Core'}))
