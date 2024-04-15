import requests

url = 'http://localhost:5000/users/1'
data = {'name': 'Charlie'}
headers = {'Content-Type': 'application/json'}

response = requests.patch(url, data=data, headers=headers)

if response.status_code == 200:
    # The request was successful
    user = response.json()
    print(user['name'])
else:
    # The request failed
    print("request failed....", response.status_code)