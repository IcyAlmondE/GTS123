arr = []
i, j, c = 0, 0, 0
while i<3 and c!=1:
    j = 0
    sub_arr = []
    while j<3 and c!=1:
        s = input("Input: ")
        if s not in "xo":
            c = 1
        else:
            sub_arr.append(s)
            j+=1
    arr.append(sub_arr)
    i+=1
if c==1:
    print("Wrong input")
else:
    for i in range(7):
        if i%2==0:
            print("-------")
        else:
            for j in range(7):
                if j%2==0:
                    print("|", end='')
                else:
                    print(arr[i//2][j//2], end='')
            print()