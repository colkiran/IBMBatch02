

def callMe():
    print(f"Apples from Ooty......")

def fun(fnc):
    print("Hello")
    fnc()
    print("Hi")
    print("-" * 20)

    def defineMe():
        print("Oranges from Kanpur.....")

    return defineMe

def funCallback(fnc):
    print("Mera Bharath Mahan.....")
    fnc()
    print("India is great......")

funCallback(fun(callMe))


