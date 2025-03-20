# Web scraping is basically sending an HTML request to a website and it extracts specific data from the website
# Beautiful Soup is a HTML parser. We will scrape data from Billboard Hot 100 and use the Spotify API to automate the playlist making process 
# pip3 install bs4, requests, python-decouple, spotipy

import requests
from bs4 import BeautifulSoup
from decouple import config
import spotipy
from spotipy.oauth2 import SpotifyOAuth
# env vars
CLIENT_ID = config("CLIENT_ID")
CLIENT_SECRET = config("CLIENT_SECRET")

URL = "https://www.billboard.com/charts/hot-100/"
# URL = "https://www.billboard.com/charts/r-b-hip-hop-songs/"
# Inspect page or view source code 
date = input("Enter a date in YYYY-MM-DD format to create a Bilboard Hot 100 album for that day: ")


# In order to emulate a web browser, we would need to use headers to make it seem like we are accessing not as bots from a python script but as actual humans 
# Broaser user agents: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/User-Agent
headers = {
   "User-Agent": "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 8_9_4) Gecko/20100101 Firefox/69.0",
   "Accept-Language": "en-US,en;q=0.9",
}

# To parse songs - websites use div elements and classes. Beautiful Soup's soup.find_all() retrieves HTML elements based on tags, classes, and IDs 
response = requests.get(URL + date, header=headers)
soup = BeautifulSoup(response.text, 'html.parser')

# web scrape to find all of the song names from the top 100
song_names = soup.find_all(name="h3", id="title-of-a-story", class_="a-no-trucate")
song_list = [song.getText().strip("\n\t") for song in song_names]
year = date.split("-")[0]

# Create a new app in spotify developer API, make sure you click the Web API button, and copy the Client ID and Client Secret ID from settings and put it in a .env file

# sp = spotipy.Spotify(
#     auth_manager=
# )


# eumoren@umass.edu --> presentor 