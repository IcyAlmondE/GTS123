s = input("Input: ")
if s.isnumeric():
    for i in s:
        for j in range(int(i)):
            if j%2==0:
                print("#", end='')
            else:
                print("*", end='')
        print()
else:
    print("Error")