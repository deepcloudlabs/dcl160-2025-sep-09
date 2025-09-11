# get distinct continents
import json
from functools import reduce


def group_by_continent(groups: dict[str,int], vector: tuple[str,int]) -> dict[str,int]:
    continent, population = vector
    groups[continent] = groups.get(continent, 0) + population
    return groups


with open("../resources/countries.json", "rt", encoding="utf-8") as file:
    countries = json.load(file)
    population_by_continent = reduce(group_by_continent, map(lambda country: (country["continent"],country["population"]), countries),{})
    for continent, population in population_by_continent.items():
        print(f"{continent}: {population}")
