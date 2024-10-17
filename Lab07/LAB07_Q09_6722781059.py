p = 0
while p==0:
    try:
        n = int(input("Enter an integer (-1 to exit): "))
        p=1
    except:
        print("Try again")
l = []
while n!=-1:
    l.append(n)
    p = 0
    while p==0:
        try:
            n = int(input("Enter an integer (-1 to exit): "))
            p=1
        except:
            print("Try again")

print("The sum of %d number(s) is %d." % (len(l), sum(l)))