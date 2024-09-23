from math import pi
d = float(input("Input a circle diameter: "))
du = input("Input a unit of the diameter: ")
au = input("Input a unit of the output area: ")
c = 0

if d>0:
    if du=='cm':
        dmm = d*10
    elif du=='in':
        dmm = d*25.4
    elif du=='mm':
        dmm = d
    else:
        c=1

    if au=='mm' and c==0:
        area = (dmm/2)**2 * pi
    elif au=='cm' and c==0:
        area = (dmm/20)**2 * pi
    elif au=='in' and c==0:
        area = (dmm/50.8)**2 * pi
    else:
        c=1

    if c==0:
        # print("The surface of a circle with a %.2f %s diameter is %.2f square %s." % (d, du, area, au))
        print(f"The surface of a circle with a {d:.2f} {du} diameter is {area:.2f} square {au}.")
    else:
        print("Invalid input")
else:
    print("Invalid input")
