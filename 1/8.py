
#Exercise 8 : Birthday Dictionaries (w/play again feature)
birthday_dictionaries = {
    "Benjamin Franklin": "17 January 1706",
    "Albert Einstein": "14 March 1879",
    "Isaac Newton": "4 January 1643"
}
play = True
while play:
    print("Welcome to the birthday dictionary. We know the birthdays of: (Please match the uppercase!)")
    keys = birthday_dictionaries.keys()
    for names in list(keys):
        print(names)
    lookup_name = str(input("Who's birthday do you want to look up?  "))
    print(birthday_dictionaries[lookup_name])
    again=str(input("Do you want to play again, type yes or no "))
    if again == "no":
      play = False