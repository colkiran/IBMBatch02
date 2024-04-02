
def outerFun(gname):

    def innerFun():

        print("Hello World")
        print(f"Greeting {gname}")
    # outerfun scope
    innerFun()

outerFun("Rahul")
