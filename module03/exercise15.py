import locale

# Set German locale (must be installed on your system)
locale.setlocale(locale.LC_ALL, "de_DE.UTF-8")

names = ["Mueller", "Müller", "Muller"]
sorted_names = sorted(names, key=locale.strxfrm)
print(sorted_names)