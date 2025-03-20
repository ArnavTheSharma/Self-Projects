# web scraping to try to find if anyone posted code 

import requests

# GitHub API endpoint
url = "https://api.github.com/search/code"

# Search for "Bus.java" with a snippet of code
query = 'Bus.java "Represents a UMass campus bus" in:file'
params = {"q": query}
headers = {"Accept": "application/vnd.github.v3+json"}

# Send request
response = requests.get(url, params=params, headers=headers)

# Check response
if response.status_code == 200:
    data = response.json()
    if data["total_count"] > 0:
        print("Bus.java found in public repositories!")
        for item in data["items"]:
            print(f"Repo: {item['repository']['html_url']} | File: {item['html_url']}")
    else:
        print("No public results found.")
else:
    print("Error:", response.status_code, response.json())
