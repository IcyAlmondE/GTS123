from math import pi

def SquareArea(x):
    return x*x

def CircleArea(r):
    return pi*r*r

c = input("Do you want to find the area of a square (s) or a circle (c)?: ")
if c=='s':
    x = float(input("Enter the lenght: "))
    print("\nThe area of the square is %.2f"%SquareArea(x))
elif c=='c':
    r = float(input("Ehter the radius: "))
    print("\nThe area of the circle is %.2f"%CircleArea(r))
else:
    print("\nWrong Input")