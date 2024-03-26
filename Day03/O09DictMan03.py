
print("items".center(60, "-"))
# is a combination of keys() and values()
emp = {'emp1' :{'name': 'Richard', 'age': 26, 'desig': 'SE', 'gender': 'Male', 'dept' : 'it', 'salary': 45000},
       'emp2' :{'name': 'Tina', 'age': 35, 'desig': 'PM', 'gender': 'female', 'dept' : 'MKT', 'salary': 125000},
       'emp3' :{'name': 'Kennedy', 'age': 30, 'desig': 'TL', 'gender': 'Male', 'dept' : 'Finance', 'salary': 75000}}

print(f"emp :{emp}")

print("-" * 60)
print(f"emp1 :{emp['emp1']}")
print("-" * 60)
print(f"emp2 :{emp['emp2']}")
print("-" * 60)
print(f"emp3 :{emp['emp3']}")
print("-" * 60)

for key, info in emp.items():
    print(key)
    print("-" * len(key))
    for k, v in info.items():
        print(k, "=>", info[k])
    print("-" * 60)

