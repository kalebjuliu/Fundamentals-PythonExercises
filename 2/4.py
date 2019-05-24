
#Exercise 4 : String List
string = str(input("Welcome to palindrome checker: Enter your word!: "))
a = []
b = []
for elem in string:
	a.append(elem)
	b = a[::-1]
def compare(list_1, list_2):
	if list_1 == list_2:
		print(f"The word {string} is palindrome")
	else:
		print(f"The word {string} is not palindrome")
compare(a, b)

input("Press enter to exit")

