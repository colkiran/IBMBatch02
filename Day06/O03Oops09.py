
from functools import total_ordering

@total_ordering
class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __str__(self):
        return f"Name is {self.name}\nSalary is {self.salary}"

    # works for not equal to also (!=)
    def __eq__(self, other):
        return self.salary == other.salary

    # Works for less than also (<)
    def __gt__(self, other):
        return self.salary > other.salary


emp1 = Employee("Peter", 45000)
print(emp1)

print("-" * 60)
emp2 = Employee("Richard", 50000)
print(emp2)

print("-" * 60)
# compares the addresses by default
if emp1 != emp2:
    print("{}'s salary of {} is NOT equal to {}'s salary of {}".format(emp1.name, emp1.salary, emp2.name, emp2.salary))
else:
    print("{}'s salary of {} is equal to {}'s salary of {}".format(emp1.name, emp1.salary, emp2.name, emp2.salary))

print("-" * 60)
if (emp1 < emp2):
    print("{}'s salary of {} is Less than {}'s salary of {}".format(emp1.name, emp1.salary, emp2.name, emp2.salary))
else:
    print("{}'s salary of {} is Greater than {}'s salary of {}".format(emp1.name, emp1.salary, emp2.name, emp2.salary))

print("-" * 60)
print(emp1 >= emp2)
print(emp1 <= emp2)







