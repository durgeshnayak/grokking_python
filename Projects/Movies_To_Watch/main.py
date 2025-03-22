import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
response = requests.get(url=URL)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

top_100_movies = []

movie_names = soup.find_all(name="h3", class_="title")
for movie in movie_names:
    top_100_movies.append(movie.text)

top_100_movies.reverse()

with open(file="movies.txt", mode="w") as file_stream:
    for movie_name in top_100_movies:
        file_stream.write(movie_name + "\n")

