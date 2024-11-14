p = 100
while 1:
    c, n = input("Command: ").split()
    if c=='done' and n=='0':
        break
    if c not in "PR" or not n.isnumeric():
        print("Invalid command")
        continue
    n = int(n)
    if c=='R':
        if n>p:
            print("Not enough points")
        else:
            print("You redeemed %d points"%n)
            p-=n
            print("Your accumulated points = %d points"%p)
    elif c=='P':
        print("You earned %d points"%(n//50))
        p+=n//50
        print("Your accumulated points = %d points"%p)