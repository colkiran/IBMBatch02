
print("keys".center(60, "-"))
player = {'name': 'Ganguly', 'age': 33, 'runs': 110, 'oppn': 'srilanka', 'venue': 'lords', 'year': '1998'}

k = player.keys()
print(f"keys :{k}")

print("-" * 60)
for k in player.keys():
    print(k, "=>", player[k])

print("values".center(60, "-"))
player = {'name': 'Ganguly', 'age': 33, 'runs': 110, 'oppn': 'srilanka', 'venue': 'lords', 'year': '1998'}
print(f"player :{player}")

print("-" * 60)
v = player.values()
print(f"v :{v}")

print("-" * 60)
for v in player.values():
    print(v, end=" ")
print()

print("fromkeys".center(60, "-"))
cities = ['blr', 'che', 'hyd', 'mum', 'del', 'kol']
print(f"cities :{cities}")

# convert the list cities into a dictionary - cities will be the key
temp = dict.fromkeys(cities)
print(f"temp :{temp}")

print("-" * 60)
temp = dict.fromkeys(cities, 23)
print(f"temp :{temp}")

print("setdefault".center(60, "-"))
player = {'name': 'Ganguly','runs': 110, 'oppn': 'srilanka', 'year': '1998'}

print(f"player :{player}")
# add new key value pairs into the dictionary
player.setdefault('age', 32)
player.setdefault('name', 'Sourav')
player.setdefault('venue', 'Gale')
player.setdefault('runs',  25)

print(f"player :{player}")

print("pop".center(60,"-" ))
player = {'name': 'Ganguly', 'age': 33, 'runs': 110, 'oppn': 'srilanka', 'venue': 'lords', 'year': '1998'}
print(f"player :{player}")

print("-" * 60)
res = player.pop('age')
print(f"res :{res}")

res = player.pop('year')
print(f"res :{res}")

print(f"player :{player}")

print("popitem".center(60, "-"))
player = {'name': 'Ganguly', 'age': 33, 'runs': 110, 'oppn': 'srilanka', 'venue': 'lords', 'year': '1998'}
print(f"player :{player}")

print("-" * 60)
res = player.popitem()
print(f"res :{res}")

res = player.popitem()
print(f"res :{res}")

print(f"player :{player}")
