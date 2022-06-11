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

response = requests.get("https://www.billboard.com/charts/hot-100/" + destination_date)

soup = BeautifulSoup(response.text, 'html.parser')
song_names_spans = soup.find_all("span", class_="chart-element__information__song")
song_names = [song.getText() for song in song_names_spans]

print(song_names)

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