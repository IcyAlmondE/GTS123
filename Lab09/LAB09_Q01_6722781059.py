from math import pi

def CirArea(x):
    return pi*x*x

def SqArea(x):
    return x*x

x = float(input("Input a positive number: "))
if x>=0:
    print("The area of the circle is %.2f"%CirArea(x))
    print("The area of the square is %.2f"%SqArea(x))
else:
    print("Wrong Input")