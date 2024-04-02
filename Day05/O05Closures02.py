
def outerFun(greet):

    # simple curry
    def innerFun(gname):

        print(greet, gname)

    return innerFun


outerFun("Welcome")('Rahul')

print("-" * 60)

EngGrt = outerFun("Welcome")
KanGrt = outerFun("Namaskara")


EngGrt("Sachin")
KanGrt("Rahul")
