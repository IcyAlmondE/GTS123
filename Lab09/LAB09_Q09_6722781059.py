from math import pi

def myCylinder(r, h):
    return pi*r*r*h, 2*pi*r*(r+h)

r = float(input("Enter the radius r of the cylinder: "))
h = float(input("Enter the height h of the cylinder: "))
print("The volume is %.2f and the surface area is %.2f"%myCylinder(r, h))