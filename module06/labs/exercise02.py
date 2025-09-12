# get distinct continents
import json
from functools import reduce


def distinct_continents(set_of_continents: set[str], continent: str) -> set[str]:
    set_of_continents.add(continent)
    return set_of_continents


with open("../resources/countries.json", "rt", encoding="utf-8") as file:
    countries = json.load(file)
    continents = sorted(reduce(distinct_continents, map(lambda country: country["continent"], countries), set()))
    print(continents)
