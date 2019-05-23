

#Exercise 5 : List Ends
a = [5, 10, 15, 20, 25]
def new_list(list):
    b = []
    b.append(list[0])
    b.append(list[-1])
    print(a, b)
new_list(a)
