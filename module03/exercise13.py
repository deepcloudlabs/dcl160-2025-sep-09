import locale

import icu
from icu import Locale
locale.setlocale(locale.LC_ALL, 'tr_TR.UTF-8')

city = "izmir"
print(city)
print(city.upper())

locale = icu.Locale("tr_TR")

city = icu.UnicodeString("izmir")
upper_city = city.toUpper(locale)
print(upper_city)