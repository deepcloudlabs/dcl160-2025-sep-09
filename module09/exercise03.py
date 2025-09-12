import re
pattern1="\\d{4}-\\d{4}-\\d{4}-\\d{4}"
credit_card = "1234-1234-1234-1234"
if re.fullmatch(pattern1, credit_card):
    print(f"{credit_card} is a valid credit card number.")