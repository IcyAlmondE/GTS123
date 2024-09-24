n = input("Input: ")
sp = ' '
if n.isnumeric():
    n = int(n)
    if n>=3:
        for i in range(n):
            for j in range(n):
                if i>=j:
                    if j%2==0:
                        print('*', end='')
                    else:
                        print('0', end='')
                else:
                    print(sp, end='')

            for j in range(n):
                if i+j>=n-1:
                    if j%2==0:
                        print('*', end='')
                    else:
                        print('0', end='')
                else:
                    print(sp, end='')
            print()
        for i in range(1, n):
            for j in range(n):
                if j<n-i:
                    if j%2==0:
                        print('*', end='')
                    else:
                        print('0', end='')
                else:
                    print(sp, end='')

            for j in range(n):
                if j>=i:
                    if j%2==0:
                        print('*', end='')
                    else:
                        print('0', end='')
                else:
                    print(sp, end='')
            print()
    else:
        print("Your input is invalid.")
else:
    print("Your input is invalid.")