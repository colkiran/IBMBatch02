
gname = "Sunil Gavaskar"

sports = ['cricket', 'tennis', 'football', 'badmiton', 'hockey', 'volleyball', 'swimming']

runs = {'test': 13500, 'odi': 16500, 't20': 2300}

def greet(gnm):
    print(f"Greeting Mr.{gnm}, welcome to the event......")

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_details(self):
        print(f"Name is {self.name}\nSalary is {self.salary}")

# __name__ = returns the module
print(__name__)
if __name__ == '__main__':
    greet(gname)

    print("-" * 60)

    emp1 = Employee("David", 12500)
    emp1.get_details()

