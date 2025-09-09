import os, requests

url = "https://api.github.com/repos/kubernetes/kubernetes/pulls"
headers = {
    "Authorization": f"Bearer {os.getenv('GITHUB_TOKEN', '')}",
    "Accept": "application/vnd.github+json",
    "X-GitHub-Api-Version": "2022-11-28",
}

## Code 1

#response = requests.get("https://api.github.com/repos/kubernetes/kubernetes/pulls")
#complete_detail = response.json()
#for i in range(len(complete_detail)):
#    print(complete_detail[i] ["user"] ["login"] )
#    print(i)

## Code 2
response = requests.get(url, headers=headers)
complete_detail = response.json()
for i in complete_detail:
    print(i["user"]["login"])