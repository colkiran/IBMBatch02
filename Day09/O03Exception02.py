
num = 10
div = 0

try:
    assert div != 0, 'Number cannot be divided by Zero.......'
    print(num / div)
except AssertionError as msg:
    print(msg)

print("-" * 60)

def set_price(val):
    assert val > 0, "The price cannot be less than zero....."
    return val

try:
    res = set_price(50)
except AssertionError as a:
    print(a)
else:
    print(f'The price is {res}')