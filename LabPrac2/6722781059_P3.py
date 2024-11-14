from operator import itemgetter

n, ns = [], []
while 1:
    s = input("Enter student name and score: ")
    if s=='end' or s=='end 0':
        break
    na, sc = s.split()
    if na in n:
        print("Duplicate name!")
        continue
    try:
        if int(sc)>100 or int(sc)<0:
            print("Invalid score!")
            continue
        n.append(na)
        ns.append([na, int(sc)])
    except:
        print("Invalid input")
c = len(ns)
print("List: ")
if c==0:
    print("> empty list!")
else:
    ns = sorted(ns, key=itemgetter(1))
    for i in range(c):
        print("%s\t%d"%(ns[c-i-1][0], ns[c-i-1][1]))