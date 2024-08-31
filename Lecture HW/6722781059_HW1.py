import math as m

r = float(input("Enter the radius of the capsule (in meters): "))
h = float(input("Enter the height of the middle cylinder (in meters): "))

v = (4/3)*m.pi*r**3 + m.pi*h*r**2
a = 4*m.pi*r**2 + 2*m.pi*r*h

print("The volume of the capsule is %.4f cubic meters" % v)
print("The surface area of the capsule is %.4f square meters" % a)