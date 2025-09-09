area_codes = {
    "ankara": 312,  # key -> value
    "istanbul": {"anadolu": 216, "avrupa": 212},
    "izmir": 232,
    "antalya": 242
}

print(area_codes)
first_city, second_city, *other_cities = area_codes  # unpacking keys
print(first_city, ": ", area_codes[first_city])
print(second_city, ": ", area_codes[second_city])
print(other_cities)
print("edirne" in area_codes)
print("ankara" in area_codes)
