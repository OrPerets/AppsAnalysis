import requests

SERVER_URL = "https://app-server-three.vercel.app/"

data = requests.get(SERVER_URL + "app7")
print(data.text)