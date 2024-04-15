
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb



plt.style.use("fivethirtyeight")

data = pd.Series(np.random.rand(1000).cumsum())
print(data)
# data.plot()
# plt.show()

print("-" * 60)

DF = pd.DataFrame(np.random.randn(1000, 4), columns=list("ABCD"))
print(DF)

DF1 = DF.cumsum()
print(DF1)

# DF1.plot()
# plt.show()

print("-" * 60)

print(DF.iloc[10])
DF.iloc[10].plot(kind = "bar")
plt.show()
