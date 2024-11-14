while 1:
    n = int(input("Enter an integer number (0 to exit): "))
    if n<0 or n>9:
        print("Valid value is between 0 and 9!")
        break
    if n==0:
        print("Exit program. Bye!")
        break
    for i in range(n):
        print(" "*(n-i-1), end="")
        for j in range(i+1):
            print(n, end=" ")
        print()
    print()