n = input("Input: ")
if n.isnumeric():
    n = int(n)
    if n>=3:
        for i in range(n):
            for j in range(n):
                if j<=i:
                    if j%2==0:
                        print("*", end='')
                    else:
                        print("0", end='')
                else:
                    print(" ", end='')
            for j in range(n):
                if j>=n-i-1:
                    if j%2==0:
                        print("*", end='')
                    else:
                        print("0", end='')
                else:
                    print(" ", end='')
            print()
        for i in range(n-1):
            for j in range(n):
                if j<n-i-1:
                    if j%2==0:
                        print("*", end='')
                    else:
                        print("0", end='')
                else:
                    print(" ", end='')
            for j in range(n):
                if j>i:
                    if j%2==0:
                        print("*", end='')
                    else:
                        print("0", end='')
                else:
                    print(" ", end='')
            print()
    else:
        print("Your input is invalid.")
else:
    print("Your input is invalid.")