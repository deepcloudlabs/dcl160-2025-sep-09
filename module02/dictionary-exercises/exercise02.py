ege = {"izmir": 232}
akdeniz = {"antalya": 242}
icanadolu = {"ankara": 312}
marmara = {"istanbul": {"anadolu": 216, "avrupa": 212}}
print(ege)
print(akdeniz)
print(marmara)
print(icanadolu)
cities = {*ege, *akdeniz, *marmara,*icanadolu}
turkey = {**ege, **akdeniz, **marmara,**icanadolu}
print(cities)
print(turkey)
