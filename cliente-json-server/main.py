import requests

obtener = requests.get("http://172.16.100.145:3000")
print(obtener.json())
