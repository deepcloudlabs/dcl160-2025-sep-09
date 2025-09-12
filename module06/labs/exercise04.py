# get distinct continents
import json
from functools import reduce


def group_by_continent(groups: dict[str,int], vector: tuple[str,int]) -> dict[str,int]:
    a_continent, a_population = vector
    groups[a_continent] = groups.get(a_continent, 0) + a_population
    return groups


with open("../resources/countries-continents.json", "rt", encoding="utf-8") as file_continents:
    with open("../resources/countries-population.json", "rt", encoding="utf-8") as file_population:
        countries_continents = json.load(file_continents)
        countries_population = json.load(file_population)
        countries_population = {country["_id"]: country["population"] for country in countries_population}
        countries = map(lambda country: (country["continent"],countries_population[country["_id"]],country["name"]) ,countries_continents)
        print(list(countries))
        population_by_continent = reduce(group_by_continent, map(lambda country: (country[0],country[1]), countries),{})
        for continent, population in population_by_continent.items():
            print(f"{continent}: {population}")
