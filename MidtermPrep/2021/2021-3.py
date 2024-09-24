s = input("Input: ")
for i in s:
    if i.isnumeric():
        for j in range(1, int(i)+1):
            if j%3==0:
                print("#", end='')
            else:
                print("*", end='')
        print()