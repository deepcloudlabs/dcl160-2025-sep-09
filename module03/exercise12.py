import icu

tr_rules = "& şi ; she & ş ; sch & s ; ş & u ; ü & i ; ı & c ; ç & o ; ö & ğ ; g & i ; İ & Ç ; c"
tr_collator = icu.RuleBasedCollator(tr_rules)

cities = ["İzmir", "Ankara", "Eskişehir", "Çanakkale", "İstanbul", "Zonguldak"]

print(cities)
print(sorted(cities,key=tr_collator.getSortKey))
