l = input("Input: ").lower().split()
d = {}
for i in l:
    if i not in d:
        d[i] = 1
    else:
        d[i] +=1
m = max(d.values())
print("Output: ")
for i in d.keys():
    if d[i]==m:
        print("%s = %d"%(i, d[i]))