

#Exercise 7 : Max of Three
a = 1
b = 5
c = 3
def max_three(num_1, num_2, num_3):
    if num_1 > num_2 and num_1 > num_3:
        print("The first number is the largest")
    elif num_2 > num_1 and num_2 > num_3:
        print("The second number is the largest")
    if num_3 > num_2 and num_3 > num_1:
        print("The third number is the largest")
max_three(a,b,c)


