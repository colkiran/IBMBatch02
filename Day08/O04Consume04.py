
# import sys
#
# for pth in sys.path:
#     print(pth)
#
# print("-" * 60)

import gurgaon.mymodule as m
from gurgaon.mymodule import Employee

m.greet("Anil Kumble")

emp1 = Employee("Thomas", 60000)
emp1.get_details()
