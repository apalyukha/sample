import json
import requests

response = requests.get("https://jsonplaceholder.typicode.com/todos")
todos = json.loads(response.text)

with open('data.txt', 'w') as outfile:
    json.dump(todos, outfile)

# True
print(todos == response.json())
# <class 'list'>
print(type(todos))
# ...
print(todos[:10])
