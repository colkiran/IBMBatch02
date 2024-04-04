
class Animal:

    def __init__(self):
        print("Animal Ctor....")
        self.__a = 10       # private Variable

    def eat(self):
        print("Animals eat.......")


class Bird(Animal):

    def fly(self):
        print("Birds fly......")

class Chicken(Bird):

    def Msg(self):
        print("This is chicken class.....")

    def fly(self):
        print("Chickens seldom fly......")


chic = Chicken()
chic.eat()          # what will happen



"""
cuckoo = Bird()
cuckoo.fly()
cuckoo.eat()
print("-" * 60)
print(cuckoo.__dict__)
# print(cuckoo._Animal__a)


# MRO - Method Resolution Order

"""