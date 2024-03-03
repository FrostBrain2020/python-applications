import requests
from bs4 import BeautifulSoup
URL = "https://www.empireonline.com/movies/features/best-movies-2/"

movies_web = requests.get(URL)
soup = BeautifulSoup(movies_web.text, "html.parser")

movies = soup.find_all(name="div", class_="listicle_listicle__item__CJna4")
with open("top100-movies.txt", mode="w") as file:
    for movie in movies[::-1]:
        file.write(f"{movie.find('h3').getText()}\n")