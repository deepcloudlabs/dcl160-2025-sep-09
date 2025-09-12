import icu

# Base collator (default locale)
base = icu.Collator.createInstance(icu.Locale("de_DE"))

# Custom collation rules: make "ü" equivalent to "ue"
rules = "&U < ü = ue"  # "ü" = composed form of ü

# Create a rule-based collator
rule_collator = icu.RuleBasedCollator(rules, base)

words = ["Mueller", "Müller", "Muller"]

# Sort using custom collator
sorted_words = sorted(words, key=rule_collator.getSortKey)

print(sorted_words)