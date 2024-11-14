b = int(input("Enter the initial balance: "))
while 1:
    x, y = input("Transaction type and amount (\"done 0\" to exit): ").split()
    if x=='done' and y=='0':
        break
    if x not in "DW" or not y.isnumeric():
        print("> Invalid transaction!")
    else:
        y = int(y)
        if x=='D':
            b+=y
            print("> Deposit = %d THB, current balance = %d THB."%(y, b))
        elif x=='W':
            b-=y
            if b<0:
                print("> Invalid transaction!")
                b+=y
            else:
                print("> Withdrawal = %d THB, current balance = %d THB."%(y, b))
print("> Current balance = %d THB."%b)