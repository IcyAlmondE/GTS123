from math import ceil, pi

p = float(input("Input the covered area for one paint bottle (cm square): "))
s = float(input("Input the number of the spheres: "))
r = float(input("Input the radius of each sphere (cm): "))

area = s*(4*pi*r**2)
b = ceil(area/p)

print("The paint bottles are needed to paint the surface of spheres is %d." % b)