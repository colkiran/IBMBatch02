
import json
import requests

BASE = "http://127.0.0.1:5000/"

print("get".center(60, "-"))
print()

response = requests.get(BASE + "getplayer/ponting")
# print(response.json())
res = response.json()

for k, info in res.items():
    print(k)
    print("-" * len(k))
    for k, v in info.items():
        print(k, "=>", v)

print("put".center(60, "-"))
print()

response = requests.put(BASE + 'getplayer/ponting', data = {'team': 'Australia'})
res = response.json()

print(res)

for k, info in res.items():
    print(k)
    print("-" * len(k))
    for k, v in info.items():
        print(k, "=>", v)

print("patch".center(60, "-"))
data = {'name': 'Sachin Ramesh Tendulkar'}

response = requests.patch(BASE + 'getplayer/sachin', json=json.dumps(data))
print(response.json())

print("post".center(60, "-"))
print()

virat = {'name':'Virat Kholi', 'runs': 23400, 'wickets':120}
response = requests.post(BASE + 'getplayer/virat', json = json.dumps(virat))
res = response.json()

for k, v in res.items():
    print(k, "=>", v)


print("delete".center(60, "-"))

response = requests.delete(BASE + 'getplayer/lara')

res = response.json()
for k, info in res.items():
    print(k)
    print("-" * len(k))
    for k, v in info.items():
        print(k, "=>", v)