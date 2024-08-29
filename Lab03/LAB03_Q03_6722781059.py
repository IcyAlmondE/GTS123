from math import *

h = float(input("Enter the pentagon height: "))
a = (h*2)/sqrt(5+2*sqrt(5))
p = 5*a
area = ((a**2)*sqrt(25+10*sqrt(5)))/4

print("The length for one side of the pentagon is %.4f" % a)
print("The pentagon area and perimeter are %.4f and %.4f" % (area, p))