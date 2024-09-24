from math import sqrt
a, b, c = input("Please enter an input: ").split('*')
ch = input("Please enter your choice (1 or 2): ")
cc=0
if a.isnumeric() and b.isnumeric() and c.isnumeric():
    a, b, c = int(a), int(b), int(c)
    if ch=='1' and a>0 and b>0 and c>0:
        ans = a + sqrt(b**2 + c**3)
    elif ch=='2' and a>0 and b>0 and c>0:
        ans = (a*b)%c
    else:
        cc=1
else:
    cc=1

if cc==0:
    print("The output is %.2f" % ans)
else:
    print("Invalid Inputs")