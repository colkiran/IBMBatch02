
# nonlocal

def outerFun(gname):        # local Variable
    print(f"before :{gname}")
    def innerFun():
        nonlocal gname
        gname = "Mr." + gname

        print("Hello World")
        print(f"Greetings {gname}")

    # outerfun
    innerFun()
    print(f"After :{gname}")

outerFun("Rahul")
