import re

raw_numbers = ["    +38(050)123-32-34",
"     0503451234",
"(050)8889900",
"38050-111-22-22",
"38050 111 22 11   ",
"067\\t123 4567",
"(095) 234-5678\\n",
"+380 44 123 4567",
"380501234567"]

def normalize_phone(phone_number):
    cleaned_number = re.sub(r'[^0-9+]','', phone_number) # replace anything that is not a number or + with empty space
    if not cleaned_number.startswith("+"):
        if cleaned_number.startswith("380"):
            cleaned_number = "+" + cleaned_number
        else:
            cleaned_number = "+38" + cleaned_number
    return cleaned_number

sanitized_numbers = [normalize_phone(num) for num in raw_numbers] #apply function to each element in a list
#sanitized_numbers= list(map(normalize_phone, raw_numbers))
print(sanitized_numbers)