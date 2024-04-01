
# named tuple - immutable dictionary
from collections import namedtuple

def ArithmeticCalc(x, y):
    sum = x + y
    diff = x - y
    prod = x * y
    quot = x / y
    nmdTpl = namedtuple("Arithmetic", "add sub mul div")
    arith = nmdTpl(add = sum, sub = diff, mul = prod, div = quot)
    return arith

res = ArithmeticCalc(20, 8)
print(res)
print(f"sum = {res.add}")
print(f"diff = {res.sub}")
print(f"prod = {res.mul}")
print(f"quot = {res.div}")


