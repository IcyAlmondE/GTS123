def UserInput():
    xl = []
    x = ""
    while x!='Done':
        x = input("Enter an input: ")
        if x.isnumeric():
            if int(x)>=0:
                xl.append(int(x))
        elif x=='Done':
            continue
        else:
            return 'Error'
    return xl

def SumOut(xl):
    s = 0
    for i in xl:
        s += i
    return s

def MinOut(xl):
    mi = xl[0]
    for i in xl:
        if i<mi:
            mi = i
    return mi

def MaxOut(xl):
    ma = xl[0]
    for i in xl:
        if i>ma:
            ma = i
    return ma

xl = UserInput()
if xl!='Error':
    print()
    print("The summation is", SumOut(xl))
    print("The minimum is", MinOut(xl))
    print("The maximum is", MaxOut(xl))
else:
    print("Error")