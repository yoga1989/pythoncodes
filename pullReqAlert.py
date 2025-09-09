import requests
#Code
url = "https://api.github.com/repos/yoga1989/pythoncodes/pulls"
response = requests.get(url).json()
#print(response)
if response:
    for i in range(len(response)):
        print(response[i]["user"]["login"] + " has 1 pull request to be approved")
else:
    print("No Pull request to approve")
