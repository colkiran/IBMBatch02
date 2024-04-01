
# variable length arguments

# *var can accept more than one value and store it in a tuple
def prodAll(*numbers):
    print(numbers)
    Prod = 1
    for number in  numbers:
        Prod *= number
    return Prod


print(prodAll(1, 2, 3, 4, 5))

print("-" * 60)

# **var will accept the data in the form of a dictionary
def extract_details(**details):
    print(details)
    for k, v in details.items():
        print(k, "=>", v)

extract_details(name="sachin", age=30, runs=100, oppn='ENG')

print("-" * 60)

def multiplyMe(x, y):
    return x * y

print(multiplyMe(10, 20))

print("-" * 60)
def ArithmeticCalc(x, y):
    sum = x + y
    diff = x - y
    prod = x * y
    quot = x / y
    return sum, diff, prod, quot

res = ArithmeticCalc(20, 8)
print(f"res :{res}")

print("-" * 60)

def fun():
    "This is a doc string"
    # this is a comment
    print("Hello World")

fun()
print(fun.__doc__)      # doc string

print("-" * 60)

def fun1(x, y):
    """

    1. if x and y are integers then we get the sum of both the numbers
    2. if x and y are strings then we get the strings concatenated
    3. if x and y are two different data types then we get an error msg
    """
    return x + y

print(fun1(10, 20))
print(fun1("hello ", "world" ))
# print(fun1(10, "hello"))

print("=" * 60)
help(fun1)