
def fun(*x):
    print(x)

fun()
fun(1)
fun(1, 2)
fun(1, 2, 3)
fun(1, 2, 3, 4)

print("-" * 60)

def sum(x, y):
    print(f"summing {x} and {y}")
    print(x + y)

def diff(x, y):
    print(f"")
    print(x - y)



def outerFun(fnc):          #HOF - higher order function
    def helperFun(*args):
        print("Logging into the service....")
        fnc(*args)
        print("Logging out of the service....")
        print("-" * 60)

    return helperFun         # HOF

sumLogger = outerFun(sum)
sumLogger(5, 8)

print("-" * 60)

difLogger = outerFun(diff)
difLogger(40, 18)

