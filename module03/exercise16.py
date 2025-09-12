import icu
import unicodedata

# Normalize strings to NFC
def normalize(text):
    return unicodedata.normalize('NFC', text)

# List of names
names = ["Müller", "Mueller", "Meier", "Müller-Lüdenscheidt"]

names = [normalize(name) for name in names]

# Base German collator
base = icu.Collator.createInstance(icu.Locale('de_DE'))

# Custom rule: treat 'ü' as 'ue'
# Use quotes for literal special characters
rules = "& 'ü' ; ue & 'Ü' ; Ue"

# Create RuleBasedCollator with base rules
rule_collator = icu.RuleBasedCollator(rules)

# Sort using custom collator
sorted_names = sorted(names, key=rule_collator.getSortKey)
print(rule_collator.compare("mueller","müller"))
print("Sorted names:", sorted_names)
