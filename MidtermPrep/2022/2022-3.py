from math import pi

v = float(input("Input a sphere volume: "))
vu = input("Input a unit of the volume: ")
ru = input("Input a unit of the sphere radius length: ")
c=0

if v>0:
    if vu=='ft':
        vin = v*12*12*12
        print(vin)
    elif vu=='in':
        vin = v
    else:
        c=1
    if c==0:
        if ru=='in':
            r = ((3*vin)/(4*pi))**(1/3)
        elif ru=='ft':
            r = (((3*vin)/(4*pi))**(1/3))/12
        else:
            c=1
    if c==0:
        print("The radius of a sphere with a volume of %.2f cubic %s is %.2f %s." % (v, vu, r, ru))
    else:
        print("Invalid input")
else:
    print("Invalid input")
