n = 0
while not 0<n<11:
    try:
        n = int(input("Enter an integer number:"))
        if not 0<n<11:
            print("1 - 10 !!!!")
    except:
        print("Input should be integer")

for i in range(n):
    for j in range(i+1):
        print(j+1, end=' ')
    print()
for i in range(n-1):
    for j in range(n-1-i):
        print(j+1, end=' ')
    print()