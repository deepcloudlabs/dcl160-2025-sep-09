# get distinct continents
import json

with open("../resources/countries.json", "rt",encoding="utf-8") as file:
    countries = json.load(file)
    continents = sorted(set(map(lambda country: country["continent"], countries)))
    print(continents)