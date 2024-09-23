m, n = input("Input: ").split()
if m.isnumeric() and n.isnumeric():
    m, n = int(m), int(n)
    if 10>m>0 and 10>n>0:
        for i in range(n):
            for j in range(m):
                if i%2==0:
                    if (i//2+j+1)%m==0:
                        print(m, end='')
                    else:
                        print((i//2+j+1)%m, end='')
                else:
                    if (m-(i//2+j))%m==0:
                        print(m, end='')
                    else:
                        print((m-(i//2+j))%m, end='')
            print()
    else:
        print("Invalid input")
else:
    print("Invalid input")
