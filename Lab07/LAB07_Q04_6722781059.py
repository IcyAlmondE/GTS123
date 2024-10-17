try:
    n = int(input("Enter an integer number:"))
    i, j = 0, 0
    while i<n:
        i+=1
        while j<n:
            j+=1
            if i==1 or j==1 or i==n or j==n:
                print("x", end=' ')
            else:
                print(" ", end=' ')
        print()
        j = 0
except:
    print("Error")