
class Player:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("Player Initialized....")

    def get_details(self):
        print(f"Name is {self.name}\nAge is {self.age}")


ply1 = Player("Sachin", 36)
ply1.get_details()

print("-" * 60)
ply2 = Player("Rahul", 32)
ply2.get_details()
ply2.runs = 50

print("-" * 60)
print(f"ply2 :{ply2.__dict__}")

print("-" * 60)
print(f"ply1 :{ply1.__dict__}")



"""
self - name of the object that made a call to the method
instance variable data will be stored in objects dictionary __dict__
ply1.__dict__

"""