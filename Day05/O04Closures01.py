

def outerFun(gname):

    def innerFun():

        print("Hello World")
        print(f"Greeting {gname}")

    # outerfun scope
    return innerFun


outerFun("Sachin")()        # directly call the innerFun

print("-" * 60)

inRef = outerFun("Rahul")
inRef()

