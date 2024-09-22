v = input("Enter speed in mph: ")
if v.isnumeric():
    v = int(v)
    s = input("Enter distance in miles: ")
    if s.isnumeric():
        s = int(s)
        if v>0 and s>0:
            f = input("Enter output format (D or M): ")
            if f=='D':
                print("At %d mph, it will take\n%.2f hours to travel %d miles." % (v, s/v, s))
            elif f=='M':
                print("At %d mph, it will take" % v)
                print("%d hours and %d minutes to travel %d miles." % (s//v, (s/v - s//v)*60, s))
            else:
                print("Invalid input")
        else:
            print("Invalid input")
    else:
        print("Invalid input")
else:
    print("Invalid input")