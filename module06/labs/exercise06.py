import json
from functools import reduce

"""
1. list the movies with multiple directors
2. count the number of movies for each genre
"""
def flat_map(iterable):
    return reduce(lambda acc,value: acc + value, iterable, [])

def genre_histogram(group,t):
    group[t[0]] = group.get(t[0],0) + t[1]
    return group

with open("../resources/movies.json", "rt", encoding="utf-8") as file:
    movies = json.load(file)
    for genre,count in reduce(genre_histogram,map(lambda _: (_,1),flat_map(map(lambda _: list(map(lambda g: g["name"] ,_["genres"])), movies))),{}).items():
        print(genre, count)

