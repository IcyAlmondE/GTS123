print("========Welcome to Hi!! Car Wash==========")
ser = input("Choose your services: W=Wash C=Wash+Vacuum >>> ")

if ser=="W":
    si = input("Enter your car size: \"S\", \"M\", \"L\" : ")

    if si == "S":
        print("Price = 100 Baht")
    elif si == "M":
        print("Price = 120 Baht")
    elif si == "L":
        print("Price = 140 Baht")
    else:
        print("You Enter the wrong car size")
elif ser=="C":
    si = input("Enter your car size: \"S\", \"M\", \"L\" : ")

    if si == "S":
        print("Price = 120 Baht")
    elif si == "M":
        print("Price = 140 Baht")
    elif si == "L":
        print("Price = 160 Baht")
    else:
        print("You Enter the wrong car size")
else:
    print("Please Choose Your Services")