
def greet():
    print("Greetings Mr.Sachin, Welcome to the event....")

def greetGst(gname):
    print(f"Greeting Mr.{gname}, Welcome to the event.....")

# city is called default arg and gname is called non default arg
def greetGstCty(gname, city="Mumbai"):
    print(f"Greetings Mr.{gname} from {city}, Welcome to the event.....")


greet()

print("-" * 60)
greetGst("Rahul")

greetGst("Sourav")

print("-" * 60)
greetGstCty("Sachin")
greetGstCty("Rohit")
greetGstCty("Rahul", "Bangalore")

# function can return values
print("-" * 60)
def fun(x):
    return x ** 2

print(fun(4))
print(fun(9))
print(fun(122))

# python supports recursive calls
# write a python code with recursive calls
#  1. to find the factorial of a numbers
#  2. to generate fibanocci series
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


number = 5
print(f"The factorial of {number} is {factorial(number)}")

print("-" * 60)

def fibo(n):
    if n == 1 or n == 0:
        return n
    else:
        return fibo(n - 1) + fibo(n - 2)

iter = int(input("Enter the number of fibanocci series to ge generated :"))
print("fibanocci series")
for i in range(iter):
    print(fibo(i), end=" ")
print()
