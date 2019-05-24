
#Exercise 7 : List Remove Duplicates
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = []
def remove_duplicates(list):
	for elem in a:
		if a.count(elem) != 1:
			a.remove(elem)
remove_duplicates(a)
print(a)

