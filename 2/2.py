
#Exercise 2 : Divisors
x = range(1, 101)
user_input = int(input("Enter a number: "))
for elem in x:
	if elem % user_input == 0:
		print(elem)
input("Press enter to exit")