
class Animal:

    def eat(self):
        print("animals eat.....")

class Bird(Animal):

    def fly(self):
        print("birds fly.....")

class Chicken(Bird):

    def Msg(self):
        print("Chickens are breeded for consumption.....")

    def fly(self):
        print("Chickens seldom fly.......")

chic = Chicken()
chic.eat()
chic.fly()
