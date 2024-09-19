from math import sqrt
x = input("Input length x: ")
x = float(x)
if 0<=x<=1000:
    rec = (((3*sqrt(3))/2)*x*x)/3
    print("The area of rectangle ABCD is %.2f" % rec)
else:
    print("Invalid length")