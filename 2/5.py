
#Exercise 5 : List Comprehensions
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
b = []
for elem in a:
	if elem % 2 == 0:
		b.append(elem)
print(b)

