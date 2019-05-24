

#Exercise 6 : Element Search 
a = [1, 3, 5, 30, 42, 43, 500]
b = 42
def check_num(list, num):
    if list.count(num) != 0:
        print(f"{num} is in the list")
        return True
    else:
        print(f"{num} is not in the list")
check_num(a, b)

