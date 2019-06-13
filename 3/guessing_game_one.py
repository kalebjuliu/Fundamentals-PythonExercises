import random

random_num = random.randint(1,10)
count = 0

def check_num(guess):
	if random_num > int(guess):
		print("Your guess is too low")
	elif random_num < int(guess):
		print("Your guess is too high")
	else:
		print("Your guess is correct !!")
		print(f"And it only took you {count} tries")


while True:
	print("Welcome to Guess the number")
	usr_input = input("Guess a number between 1 - 10: ")
	
	if usr_input != "exit":
		check_num(usr_input)
		count += 1
	else:
		print("Goodbye")
		break

