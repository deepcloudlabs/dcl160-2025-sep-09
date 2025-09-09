area_codes = {
    "ankara": 312, # key -> value
    "istanbul": {"anadolu": 216, "avrupa": 212},
    "izmir": 232
}

print(area_codes["ankara"]) # 312
print(area_codes["istanbul"]["avrupa"]) # 212
print(area_codes["izmir"]) # 232

print(list(area_codes.keys()))
print(list(area_codes.values()))
print(list(area_codes.items()))