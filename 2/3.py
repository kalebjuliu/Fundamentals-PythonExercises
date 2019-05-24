
#Exercise 3 : List Overlap
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 21, 12, 13]
c = []
for elem in a:
	if b.count(elem) == 1:
		c.append(elem)
print(set(c))

