import requests

response = requests.get("https://api.github.com/repos/kubernetes/kubernetes/pulls")
conversion = response.json()
for list in conversion:
    print(list["user"]["login"])

