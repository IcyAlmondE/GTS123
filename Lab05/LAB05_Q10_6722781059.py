s = input("Input: ")
check = 0
for i in s:
    if i not in ["X", "O", "."]:
        check = 1
        break
if len(s)==9 and check==0:
    for i in range(7):
        if i%2==0:
            print("-------")
        else:
            print("|%s|%s|%s|" % (s[(i//2)*3], s[(i//2)*3+1], s[(i//2)*3+2]))
else:
    print("Error")