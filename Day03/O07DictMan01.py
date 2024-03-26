
d1 = dict()
print(f"d1 :{d1}")
print(type(d1))

print("-" * 60)
d2 = {'name': 'sachin', 'runs': 120, 'oppn': 'WI', 'loc': 'sabina park'}
print(f"d2 :{d2}")
print(type(d2))

print("-" * 60)
d3 = dict(name='Rahul', age=29, runs=80, oppn='Aus', venue='MCG')
print(F"d3 :{d3}")
print(type(d3))

print("-" * 60)
d4 = dict([('name', 'sehwag'), ('age', 32), ('runs', 65), ('oppn', 'NZL'), ('venue', 'eden park')])
print(f"d4 :{d4}")
print(type(d4))

print("-" * 60)
# CRUD dictionary
# create

player = {'name': 'Sourav', 'age': 33, 'runs': 110, 'oppn': 'srilanka', 'venue': 'lords'}
print(f"player :{player}")

print("-" * 60)
# read
print(f"Name :{player['name']}")
print(f"Runs :{player['runs']}")
print(f"opponent :{player['oppn']}")

print("-" * 60)
# iterate
for i in player:
    print(i + " => " + str(player[i]))

print("-" * 60)
# update, add
player['name'] = 'Ganguly'
player['year'] = '1998'
print(f"player :{player}")

print("-" * 60)
# deletion
del player['age']
print(f"player :{player}")

print("-" * 60)
# print(dir(player))
