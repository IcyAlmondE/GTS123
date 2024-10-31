def LeftRotate(x, n):
    nx = []
    for i in range(len(x)):
        nx.append(x[(i+n)%len(x)])
    return nx

def RightRotate(x, n):
    nx = []
    for i in range(len(x)):
        nx.append(x[(i-n)%len(x)])
    return nx

x = input("Enter 5 inputs: ").split()
try:
    n = int(input("Enter an integer number of rotations (0-%d): "%(len(x)-1)))
    ch = x[n]
    print("The left rotated list:", LeftRotate(x, n))
    print("The right-rotated list:", RightRotate(x, n))
except:
    print("Error!")