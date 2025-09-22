import os
import json
import requests

API_KEY =  "AIzaSyBJmmbBDSiq9wrj5TW9f4gsvQsc0tFGKhE"
CSE_ID = "e4a994a14e71e4594"

base_dir = os.path.dirname(__file__)
file_path = os.path.join(base_dir, "listAidworks.json")


with open(file_path, "r", encoding="utf-8") as f:
    names2 = json.load(f)

print(len(names2))


def google_search(query, api_key, cse_id):
    url = "https://www.googleapis.com/customsearch/v1"
    res = requests.get(url, params={"q":query, "key":api_key, "cx":cse_id})
    return res.json()

linkedinUrls = []

for i in range(0, len(names2)):
    query = f'{names2[i]} "Shrewsbury High School" site:linkedin.com/in'
    results = google_search(query, API_KEY, CSE_ID)

    for r in results.get("items", []):
        link = r.get("link")
        if "linkedin.com/in" in link:
            linkedinUrls.append(link)
            print(f'{names2[i]} --> {link}')


print(linkedinUrls)