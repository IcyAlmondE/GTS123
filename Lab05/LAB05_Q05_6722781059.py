n = input("enter no. of lines: ")
if n.isnumeric():
    n = int(n)
    if n>=0:
        for i in range(1, n+1):
            if i%2==1:
                print("-"*i)
            else:
                print("*"*i)
    else:
        print("Error")
else:
    print("Error")