
def outerFun(greet):

    def innerFun(sep):

        def innerMostFun(name):
            from emojis import emojis

            emojized = emojis.encode(greet + " :" + sep + ": " + name)

            print(emojized)

        return innerMostFun

    return innerFun

KanGrt = outerFun("Namaskara")
TgrKanGrt = KanGrt("tiger")

TgrKanGrt("Prabhakar")







"""
EngGrt = outerFun("Welcome")
KanGrt = outerFun("Namaskara")

SngArw_EngGrt = EngGrt("------>")
DblArw_KanGrt = KanGrt("======>")

SngArw_EngGrt("Sachin")
DblArw_KanGrt("Rahul")
"""