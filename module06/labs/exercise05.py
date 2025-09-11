import json
"""
1. list the movies with multiple directors
2. count the number of movies for each genre
"""
with open("../resources/movies.json", "rt", encoding="utf-8") as file:
    movies = json.load(file)
    for movie in filter(lambda _: len(_["directors"]) > 1, movies):
        print(f"https://www.imdb.com/title/{movie["imdb"]}")

