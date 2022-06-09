from bs4 import BeautifulSoup
import requests

destination_date = input("What time period would you like to travel to? (format in YYYY-MM-DD) ")

response = requests.get("https://www.billboard.com/charts/hot-100/" + destination_date)

soup = BeautifulSoup(response.text, 'html.parser')
song_names_spans = soup.find_all("span", class_="chart-element__information__song")
song_names = [song.getText() for song in song_names_spans]