s = input(("Input: "))
a, b = s.split()

if a.isnumeric() and b.isnumeric:
    a, b = int(a), int(b)
    if 0<a<10 and 0<b<10:
        for i in range(b):
            if i%2==0:
                for j in range(a):
                    if (i//2+j+1)%a==0:
                        print(a, end='')
                    else:
                        print((i//2+j+1)%a, end='')
                print()
            else:
                for j in range(a):
                    if (a-(i//2+j))%a==0:
                        print(a, end='')
                    else:
                        print((a-(i//2+j))%a, end='')
                print()
    else:
        print("Invalid input")
else:
        print("Invalid input")