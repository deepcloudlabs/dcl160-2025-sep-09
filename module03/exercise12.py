name1 = "mueller"
name2 = "müller"
# collation
print(name1.__eq__(name2))
print(name1 == name2) # operator overloading

# locale
city = "izmir"
print(city)
print(city.upper())

cities = ["İzmir", "Ankara", "Eskişehir", "Çanakkale", "İstanbul", "Zonguldak"]
print(cities)
print(sorted(cities))