import requests
import json

target ="https://jsonplaceholder.typicode.com/users"
response = requests.get(url=target)
data = response.json()
usernames=[]
for userdata in data:
    # print(userdata)
    username = userdata['name']
    usernames.append(username)
print(usernames)