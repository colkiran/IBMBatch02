

class Player:

   def __init__(self, name, age):
       self.name = name
       self.age = age

   def get_details(self):
       print(f"Name is {self.name}\nAge is {self.age}")

   @staticmethod
   def CalcAge(stdt, eddt):
       from datetime import datetime
       stdt = datetime.strptime(str(stdt), "%d-%m-%Y")
       eddt = datetime.strptime(str(eddt), "%Y-%d-%m")
       totalDays = (eddt - stdt).days
       age = round(totalDays / 365,2)
       return age


   @classmethod
   def CreatePlayer(cls, name, dob):
       from datetime import date
       # convert the dob to age and call the constructor
       dt1 = dob
       dt2 = date.today()
       age = Player.CalcAge(dt1, dt2)
       return cls(name, age)

ply1 = Player.CreatePlayer("Jack", "05-08-1985")
ply1.get_details()
