
import requests

BASE = "http://127.0.0.1:5000/"

response = requests.get(BASE + "getplayer/ponting")
# print(response.json())
res = response.json()

for k, info in res.items():
    print(k)
    print("-" * len(k))
    for k, v in info.items():
        print(k, "=>", v)

print("-" * 60)

response = requests.put(BASE + 'getplayer/ponting', data = {'team': 'Australia'})
res = response.json()

print(res)

for k, info in res.items():
    print(k)
    print("-" * len(k))
    for k, v in info.items():
        print(k, "=>", v)

print("-" * 60)

response = requests.post(BASE + 'getplayer/virat', data =  {'virat': {'name': 'Virat Kholi', 'runs': 23400, 'wickets': 120}})
res = response.json()
print(res)

print("-" * 60)

response = requests.delete(BASE + 'getplayer/lara')

res = response.json()
for k, info in res.items():
    print(k)
    print("-" * len(k))
    for k, v in info.items():
        print(k, "=>", v)