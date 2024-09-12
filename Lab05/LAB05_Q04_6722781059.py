n = input("Enter an integer number (n>0): ")
if n.isnumeric():
    n = int(n)
    if n>0:
        print("(1) Factorial of n (n!)\n(2) Summation of n integers")
        op = input("Select operation: ")

        if op=='1':
            p = 1
            for i in range(1, n+1):
                p*=i
            print("Factorial of n (n!) =", p)
        elif op=='2':
            s = 0
            for i in range(1, n+1):
                s+=i
            print("Summation of n integers =", s)
        else:
            print("N/A Operation!")
    else:
        print("N/A Operation!")
else:
    print("Error")