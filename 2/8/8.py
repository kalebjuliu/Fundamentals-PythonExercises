
#Exercise 7 : List Remove Duplicates
import random

with open('D:/Work/Coding Projects/Python Projects/Tutorials/2/8/words.txt', 'r') as open_file:
	all_text = open_file.read().splitlines()
	open_file.close()


def main(text_file):
	words_list = []
	for elem in text_file:
		words_list.append(elem)

	random_number = random.randint(1, 267750)
	random_word = words_list[random_number]

	word_list = []
	for elem in random_word:
		word_list.append(elem)
	return word_list


word = main(all_text)
guessed = "_" * len(word)
guessed = list(guessed)
lstGuessed = []
letter = input("guess letter: ")
while True:
	if letter.upper() in lstGuessed:
		letter = ''
		print("Already guessed!!")
	elif letter.upper() in word:
		index = word.index(letter.upper())
		guessed[index] = letter.upper()
		word[index] = '_'
	else:
		print(''.join(guessed))
		if letter is not '':
			lstGuessed.append(letter.upper())
		letter = input("guess letter: ")

	if '_' not in guessed:
		print("You won!!")
		break






