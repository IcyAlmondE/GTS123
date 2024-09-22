a = input("Input: a=? ")
b = input("Input: b=? ")
c = input("Input: c=? ")

if a.isnumeric() and b.isnumeric() and c.isnumeric():
    a, b, c = int(a), int(b), int(c)
    if a+b>c and b+c>a and c+a>b:
        print("Output: Form a triangle")
    else:
        print("Can't form a triangle")
else:
    print("Some input is not a number")