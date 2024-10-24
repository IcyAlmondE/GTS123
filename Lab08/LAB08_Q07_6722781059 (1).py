l = []
numseq = 2
res = set()

for i in range(numseq):
    l.append(input("Input sequence%s: "%(i+1)).split())
    ls = set()
    for j in l[i]:
        if j.isnumeric():
            ls.add(j)
    if i==0:
        res = ls
    else:
        res = res&ls

if len(res)>0:
    print("Output: True")
else:
    print("Output: False")