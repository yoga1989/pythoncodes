import os, requests

url = "https://api.github.com/repos/kubernetes/kubernetes/pulls"
headers = {
    "Authorization": f"Bearer {os.getenv('GITHUB_TOKEN', '')}",
    "Accept": "application/vnd.github+json",
    "X-GitHub-Api-Version": "2022-11-28",
}
response = requests.get(url, headers=headers)
### print(response) ---> responds 200 which is good
converted_file = response.json()
# print(converted_file) # ---> Check ok
for i in range(len(converted_file)):
    #print(i)
    print(converted_file[i]["user"]["login"])
    print(converted_file[i]["number"])