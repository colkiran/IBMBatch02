
class Employee:

    def __init__(self, name):
        self.__name = name
        self.tech = ['C', 'C++', 'JAVA', 'AngularJS','ReactJS']

    def __str__(self):
        return self.__name + " " + ",".join(self.tech)

emp1 = Employee("Jack")
print(emp1)
# print(emp1.__name)
print(emp1.__dict__)
emp1._Employee__name = "Louis"
print(emp1)
