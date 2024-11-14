d = {}
while 1:
    s = input("Input: ")
    if s=='done':
        break
    if not s.isnumeric() or not (0<int(s)<1001):
        print("ERROR")
        continue
    s = int(s)
    if s not in d:
        d[s] = 1
    else:
        d[s]+=1
print("----SUMMARY----")
if len(d)==0:
    print("The list is empty")
else:
    dl = sorted(d)
    for i in dl:
        print("%d %d"%(i, d[i]))