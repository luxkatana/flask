import requests

get = requests.get("http://127.0.0.1/api", params={"robloxID": 800926308})

print(get.json())