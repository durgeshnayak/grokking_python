import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy import SpotifyClientCredentials
from spotipy import SpotifyOAuth
import pprint

SPOTIPY_CLIENT_ID = "ed6f51886886487eb3e170b1f717ffe3"
SPOTIPY_CLIENT_SECRET = "871e40d42e394d77a9f4a45194390042"

date_chart = input("Please enter the date that you would like the top 100 songs for (YYYY-MM-DD): ")

response = requests.get(url=f"https://www.billboard.com/charts/hot-100/{date_chart}")
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

song_names_headers = soup.select(selector="li ul li h3")
song_names = []

for song in song_names_headers:
    song_names.append(song.get_text(strip=True))

# auth_manager = SpotifyClientCredentials(client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET)
auth_manager = SpotifyOAuth(
    client_id=SPOTIPY_CLIENT_ID,
    client_secret=SPOTIPY_CLIENT_SECRET,
    redirect_uri="http://example.com",
    scope="playlist-modify-private",
    show_dialog=True,
    cache_path="token.txt"
)
sp = spotipy.Spotify(auth_manager=auth_manager)

user_id = sp.current_user()["id"]
lst_track_uri = []
for song_name in song_names:
    search_query = f"track: {song_name} year: {date_chart.split('-')[0]}"
    search_result = sp.search(q=search_query, type="track")

    try:
        track_uri = search_result["tracks"]["items"][0]["uri"]
    except IndexError:
        print(f"Track {song_name} not available in Spotify hence skipping...")
    else:
        lst_track_uri.append(track_uri)

playlist = sp.user_playlist_create(user=user_id,
                                   name=f"{date_chart} Billboard 100",
                                   public=False,
                                   description=f"Hits from {date_chart} Billboard 100")

playlist_id = playlist["id"]

playlist_add_response = sp.playlist_add_items(playlist_id=playlist_id, items=lst_track_uri)
pprint.pprint(playlist_add_response)
