
def funLogger(fnc):
    def helper():
        print("My info logged in a Service....")
        fnc()
        print("My info logged out of service......")
        print("-" * 60)

    return helper


def normalfun():
    print("I should be called as normal Function.....")

funLogger(normalfun)
print("-" * 60)

funLogger(normalfun)()
print("-" * 60)

normalfun = funLogger(normalfun)
normalfun()

@funLogger              # decorator - basicfun = funLogger(basicFun)
def basicFun():
    print("I should be called as BASIC")

basicFun()