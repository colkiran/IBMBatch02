
import sys

sys.path.append("C:\\Delhi")

for pth in sys.path:
    print(pth)

print("-" * 60)

import gurgaon.mymodule as m

m.greet("Sourav Ganguly")