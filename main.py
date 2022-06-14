from bs4 import BeautifulSoup
import requests

movies = []
site = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(site)
soup = BeautifulSoup(response.text, "html.parser")

for row in soup.find_all("h3"):
    movies.append(row.text)

for i in reversed(range(0, 100)):
    with open("movies.txt", "a") as txt:
        txt.write(f"{movies[i]} \n")