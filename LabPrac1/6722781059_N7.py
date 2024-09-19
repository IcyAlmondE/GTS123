from math import sqrt

s = input("Input the area of A and C: ")
a, c = s.split()
a, c = float(a), float(c)
if c>a and 0<=a<=1500 and 0<=c<=1500:
    b = c - a
    print("The area of the triangle is %.2f" % ((sqrt(a)*sqrt(b))/2))
else:
    print("Invalid areas")