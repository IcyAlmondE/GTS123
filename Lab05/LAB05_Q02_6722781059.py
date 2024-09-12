s = 0

for i in range(1, 6):
    x = input("Enter an integer #%d: " % i)
    if x.isnumeric():
        s += int(x)

print("The summation is %d." % s)