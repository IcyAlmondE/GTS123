from math import floor
cube = float(input("Enter the width of the cube: "))
w = float(input("Enter the width of the container: "))
h = float(input("Enter the height of the container: "))
d = float(input("Enter the depth of the container: "))

wcu = floor(w/cube)
hcu = floor(h/cube)
dcu = floor(d/cube)

n = wcu*hcu*dcu

print("The number of cubes that can fit into the container is %d." % n)