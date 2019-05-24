
#Exercise 1 : List Less Than
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = []
user_input = int(input("Enter a number "))
for num in a:
    if num < user_input:
        b.append(num)
print(b)
input("Press enter to exit")
        

