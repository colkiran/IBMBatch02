
import numpy as np
import seaborn as sb

sb.set(style = "white")

res = np.random.RandomState(10)
d = res.normal(size=50)

sb.distplot(d, kde=True, color='g')