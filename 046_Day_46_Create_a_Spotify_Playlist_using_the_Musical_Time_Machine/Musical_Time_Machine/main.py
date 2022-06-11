from bs4 import BeautifulSoup
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import requests
import spotipy
import os

load_dotenv(r'.env')

spotify_client_id=os.getenv("CLIENTID")
spotify_secret=os.getenv("CLIENTSECRET")

destination_date = input("What time period would you like to travel to? (format in YYYY-MM-DD) ")
year = destination_date[:4]

response = requests.get("https://www.billboard.com/charts/hot-100/" + destination_date)

soup = BeautifulSoup(response.text, 'html.parser')
song_names_spans = soup.select(selector="li h3", id="title-of-a-story")
song_names = [song.getText().strip() for song in song_names_spans]
song_names = song_names[0:100]

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="https://example.com/callback",
        client_id=spotify_client_id,
        client_secret=spotify_secret,
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]

print(user_id)

query = f"track: {song_names[0]} year: {year}"
search_results = sp.search(q=query, limit=1)
print(search_results['tracks']['items'][0]['uri'])

spotify_song_uris = []

print(f"===========Searching for Spotify URI for TRACKS===========")
for song_name in song_names:
  query = f"track: {song_name} year: {year}"
  search_results = sp.search(q=query, limit=1)
  try:
    current_song_uri = search_results['tracks']['items'][0]['uri']
    print(f"Found Spotify URI for TRACK: {song_name}")
  except: 
    print("===================================================================")
    print(f"No Spotify URI found for TRACK: {song_name}")
    print("===================================================================")
  spotify_song_uris.append(current_song_uri)

print(f"===========SEARCH COMPLETE===========\n")

playlist_name = f"{destination_date} Billboard 100"
playlist_description = f"Contains all of the 100 top played songs determined by www.billboard.com/charts/hot-100 from this period of time: {destination_date}"

playlist = sp.user_playlist_create(user_id, name=playlist_name, public=False, collaborative=False, description=playlist_description)
playlist_id = playlist['id']
playlist_uri = playlist['uri']

sp.playlist_add_items(playlist_id = playlist_id, items = spotify_song_uris)

print(f"===========PLAYLIST: {playlist_name} CREATED: {playlist_uri}===========")