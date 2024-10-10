dmy = input("Enter dd/mm/yyyy: ")

if len(dmy)==8:
    d = int(dmy[0:2])
    m = int(dmy[2:4])
    y = int(dmy[4:])

    if m>12:
        print("Error! There're 12 months")
    else:
        print("Date = %02d"% d)
        print("Month =", m)
        print("Year =", y-543)
else:
    print("Please enter 8 digits!!")