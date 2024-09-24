ch = input("Enter a special character: ")
si = input("Enter the size of the pattern: ")
op = input("Enter option for the pattern: ")

if ch in ['#', '$', '@', '*', '^'] and op in ['1', '2'] and si.isnumeric():
    si = int(si)
    if op=='1':
        for i in range(si):
            for j in range(si):
                if i==j:
                    print(ch, end=' ')
                else:
                    print('.', end=' ')
            print()
    else:
        for i in range(si):
            for j in range(si):
                if i+j==si-1:
                    print(ch, end=' ')
                else:
                    print('.', end=' ')
            print()
else:
    print("Wrong input values.")