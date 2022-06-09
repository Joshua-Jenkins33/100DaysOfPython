# Day 46: Create a Spotify Playlist using the Musical Time Machine

What does a musical time machine mean? Music can take you back to a period of time in your life; reliving your childhood! Particular memories or relationships. This project will go back in time to find the music that was in the top 100 charts so you can relive that period of time once more through music.

We're going to:
1. We're going to use beautiful soup to scrape the top 100 songs from a particular date of your choice
2. Extract song titles from the list 
3. Use spotify api to create a new playlist for that date
4. Search through spotify for those songs and add them to the playlist

## Step: 1 Scraping the Billboard Hot 100

1. Create a new project in PyCharm and create the main.py file.
- [x] Complete

2. Create an input() prompt that asks what year you would like to travel to in YYY-MM-DD format. e.g.
- [x] Complete

3. Using what you've learnt about BeautifulSoup, scrape the top 100 song titles on that date into a Python List.
- [x] Complete

Hint: Take a look at the URL of the chart on a historical date: https://www.billboard.com/charts/hot-100/2000-08-12

```py
from bs4 import BeautifulSoup
import requests

destination_date = input("What time period would you like to travel to? (format in YYYY-MM-DD) ")

response = requests.get("https://www.billboard.com/charts/hot-100/" + destination_date)

soup = BeautifulSoup(response.text, 'html.parser')
song_names_spans = soup.find_all("span", class_="chart-element__information__song")
song_names = [song.getText() for song in song_names_spans]
```

[SOLUTION](https://gist.github.com/angelabauer/0fb1ca02de8f96c79830e0184a1f405c)

## Step: 2 Authentication with Spotify

## Step: 3 Search Spotify for the Songs from Step 1

## Step: 4 Creating and Adding to the Spotify Playlist