
class Employee:
    def __init__(self, name):
        self.name = name
        self.tech = ['C', 'C++', 'Java', 'Angular', 'React', 'Oracle']

    def __str__(self):
        return f"Name is {self.name}\nTech is {self.tech}"

    def __iter__(self):
        return iter(self.tech)

    def __getitem__(self, idx):
        return self.tech[idx]

    def __setitem__(self, key, value):
        self.tech[key] = value

emp1 = Employee("Mark")
print(emp1)

print("-" * 60)
for e in emp1:
    print(e, end=" ")
print()

print("-" * 60)
x = emp1[2]
print(f"x :{x}")

print("-" * 60)
emp1[2] = "Dotnet"

for e in emp1:
    print(e, end=" ")
print()


