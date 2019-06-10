import json

with open("info.json", "r") as f:
    info = json.load(f)

info_names = list(info.keys())
info_birthdays = list(info.values())

run = True
while run:
    print("Welcome to the birthday dictionary. We know the birthdays of: (Please match the uppercase!)")
    for names in info_names:
        print(names)
        
    lookup_name = str(input("Who's birthday do you want to look up?  "))
    print(info[lookup_name])
    
    again=str(input("Do you want to play again, type yes or no "))
    if again == "no":
        run = False  

