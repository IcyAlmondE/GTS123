l = input("Input: ").split()
d = {}
for i in l:
    if i.isnumeric() and i not in d:
        d[i] = 1
    elif i.isnumeric():
        d[i] +=1
good = True
for i in d.keys():
    if int(i)!=d[i]:
        good = False
if good:
    print("Output: good sequence")
else:
    print("Output: not good sequence")