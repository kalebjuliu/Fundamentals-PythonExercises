import random

choices = ["Rock", "Paper", "Scissors"]
comp_choice = random.choice(choices)

def check_winner_user(user, comp):
	if user == "Rock" and comp == "Scissors":
		print("User Wins and the computer pick", comp_choice)
	elif user == "Scissors" and comp == "Paper":
		print("User Wins and the computer pick", comp_choice)
	elif user == "Paper" and comp == "Rock":
		print("User Wines and the computer pick", comp_choice)
	elif user == comp:
		print("Its a tie")
	else:
		print("Comp Wins", comp_choice)

while True:
	print("Welcome to Rock Paper Scissors")
	usr_command = str(input("Do you want to play? (yes/no) "))
	if usr_command == "no":
		break
	else:
		usr_choice = str(input("Well then, pick between Rock, Paper and Scissors: "))
		check_winner_user(usr_choice, comp_choice)


