
#Exercise 4 : Odd or Even
num = int(input("Input a number! "))
if num%4 == 0 and num%2 == 0:
    print(f"{num} is a multiple of 4")
elif num%2 == 0:
    print(f"{num} is an even number")
elif num%2 != 0:
    print(f"{num} is an odd number")
input("Press enter to exit")

