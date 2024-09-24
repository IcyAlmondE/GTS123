from math import sqrt
a, b = input("Please enter two integers: ").split()
if a.isnumeric() and b.isnumeric():
    a, b = int(a), int(b)
    if 0<a<=30 and 0<b<=30:
        u = max(a, b)
        d = min(a, b)
        s = sum(range(d, u+1))
        print("The minimum number is", d)
        print("The maximum number is", u)
        print("The square root of the summation is %.2f" % sqrt(s))
    else:
        print("Invalid Inputs")
else:
    print("Invalid Inputs")