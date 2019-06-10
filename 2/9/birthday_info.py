import json

birthday_dict = {
    "Benjamin Franklin": "17 January 1706",
    "Albert Einstein": "14 March 1879",
    "Isaac Newton": "4 January 1643"
}

with open("info.json", "w") as f:
    json.dump(birthday_dict, f)
