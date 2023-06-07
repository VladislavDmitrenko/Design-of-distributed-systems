import requests
import json
import uuid

# Виконання POST-запиту
msg = "Hello, World!"
data = {"msg": msg}
headers = {'Content-Type': 'application/json'}
url = "http://localhost:8000/"
response = requests.post(url, data=json.dumps(data), headers=headers)
print(response.text)

# Виконання GET-запиту
url = "http://localhost:8000/"
response = requests.get(url)
print(response.text)