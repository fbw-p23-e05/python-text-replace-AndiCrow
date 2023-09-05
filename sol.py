text = "A dogmatic dog buys dogecoin to become rich and buy hotdogs every day."
# dog = text.replace(" dog ", " cat ")
# print(f"{dog}")


import re

dog = re.search("dog ", text)

if dog:
    match_text = dog.group()
    text = text.replace(match_text, "cat ")
    print(text)
else:
    print("No cats were found")



