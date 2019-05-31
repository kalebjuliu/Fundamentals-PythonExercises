import math

print("Welcome to EZQuadratic!")

a = int(input("Enter value of a: "))
b = int(input("Enter value of b: "))
c = int(input("Enter value of c: "))

d = int((b**2) - (4*a*c))
x = math.sqrt(d)

print(x)

