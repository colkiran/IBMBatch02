
class Animal:
    def __init__(self):
        print("Animal Ctor.....")
        self.a  = 10
    def eat(self):
        print("Animals eat......")

    def fun(self):
        print("fun method of Animal class")

class Person:

    def __init__(self):
        print("Parent Ctor.....")
        self.p = 10

    def talk(self):
        print("Person talks")

    def fun(self):
        print("fun method of Person Class.....")


class Girl(Animal, Person):

    def __init__(self):
        super().__init__()          # call the parent class constructor
        Person.__init__(self)
        print("Girl Ctor......")
        self.g = 30


grace = Girl()
print("-" * 60)

grace.talk()
grace.eat()
print("-" * 60)

grace.fun()

print("-" * 60)
print(grace.__dict__)
