n = input("Enter an integer number (\'X\' to exit): ")
while n!='X':
    try:
        n = int(n)
        for i in range(n):
            for j in range(n):
                if i==j or i==n-j-1:
                    print("X", end=' ')
                else:
                    print(".", end=' ')
            print()

    except:
        print()
    n = input("Enter an integer number (\'X\' to exit): ")