n = int(input("Input: "))
c = 1
if 1<=n<=15:
    for i in range(n):
        for j in range(n):
            if i<=j:
                print(c, end="\t")
                c+=1
            else:
                print(0, end="\t")
        print()
else:
    print("Invalid input")