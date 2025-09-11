# get distinct continents
import json
from functools import reduce


def distinct_continents(conts: set[str], continent: str) -> set[str]:
    conts.add(continent)
    return conts


with open("../resources/countries.json", "rt", encoding="utf-8") as file:
    countries = json.load(file)
    continents = sorted(reduce(distinct_continents, map(lambda country: country["continent"], countries), set()))
    print(continents)
