import requests

BASE = "http://127.0.0.1:5000/"

data = [{"likes": 78, "name": "Sushant", "views":100000},
		{"likes": 10000, "name": "How to make Rest API", "views":800000},
		{"likes": 10, "name": "Parth", "views":2000}]

response = requests.delete(BASE+"video/0")
response = requests.get(BASE + "video/1")
print(response.json())
input
response = requests.patch(BASE + "video/2", {})
print(response.json())
input
response = requests.put(BASE + "video/3")
