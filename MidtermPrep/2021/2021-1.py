from math import pi

s = input("Input a shape T/S/C: ")
d = input("Input a length: ")
c = 0
if s not in ['T', 'S', 'C']:
    print("Type must be only T/S/C.")
    c = 1
if not d.isnumeric():
    print("Length must be more than or equal to zero.")
    c = 1

if c==0:
    d = int(d)
    if s=='T':
        print("The surface area of triangle is %.2f" % (d**2 /4))
    elif s=='S':
        print("The surface area of square is %.2f" % (d**2 /2))
    else:
        print("The surface area of circle is %.2f" % (pi*d**2 /4))