
class Player:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_details(self):
        print(f"Name is {self.name}\nAge is {self.age}")

    @staticmethod
    def static_method01():
        print("This is a static method")

    def test(self):
        Player.static_method01()


ply1 = Player("Rahul", 29)
ply1.get_details()
ply1.test()         # call the static method


print("-" * 60)
Player.static_method01()