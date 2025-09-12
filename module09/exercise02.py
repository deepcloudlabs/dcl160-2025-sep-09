import re

meyveler = ["elma", "armut", "kiraz", "nar", "şeftali", "muz",
            "karpuz", "kavun", "kivi", "böğürtlen", "vişne", "karadut",
            "çilek", "kızılcık", "incir", "frenk üzümü", "ahududu", "12345"
            ]
pattern1 = "...."
pattern2 = "[a-zA-Z][a-zA-Z][a-zA-Z][a-zA-Z]"
pattern3 = "[a-zA-Züğiçşö]{5}"
pattern4 = "[a-zA-Züğiçşö ]{4,}"
pattern5 = "[a-zA-Züğiçşö]{,4}"
pattern6 = "[a-zA-Züğiçşö]{4,6}"
pattern7 = "[0-9]{5}"
pattern8 = "\\d{5}"
pattern9 = "[a-zA-Züğiçşö ]{4}[a-zA-Züğiçşö ]+"
for meyve in meyveler:
    if re.fullmatch(pattern7, meyve):
        print(meyve)