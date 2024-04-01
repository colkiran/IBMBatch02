
print("get".center(60,"-"))
player = {'name': 'Rahul', 'age': 32, 'runs': 120, 'oppn': 'SA'}
print(f"Player :{player}")

print(f"Name :{player.get('name', 'Invalid Key')}")
print(f"Runs :{player.get('run', 'Invalid Key')}")

print("setdefault".center(60, "-"))
player = {'name': 'Rahul', 'age': 32, 'runs': 120, 'oppn': 'SA'}
print(f"Player :{player}")

# it will only allow us to add a new key value pair
player.setdefault('name', 'Dravid')
player.setdefault('venue', 'chinnaswamy')
player.setdefault('age', 29)
player.setdefault('gender', 'male')

print(f"player :{player}")

print("Update".center(60, "-"))
emp1 = {'name': 'Richard', 'age': 26,  'gender': 'Male', 'dept' : 'it', 'salary': 45000}
emp2 = {'name': 'Tina', 'age': 35, 'desig': 'PM', 'gender': 'female', 'dept' : 'MKT'}

print(f"emp1 :{emp1}")
print(f"emp2 :{emp2}")

print("-" * 60)

# updating the values of emp1 with emp2
emp1.update(emp2)
print(f"emp1 :{emp1}")

