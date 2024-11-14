from operator import itemgetter

def avg(l):
    return sum(l)/len(l)

n, sco, ns = [], [], []
while 1:
    s = input("Input: ")
    if s=='done':
        break
    na, sc = s.split()
    if not sc.isnumeric():
        print("Invalid input")
        continue
    if na in n:
        print("Duplicated player")
        continue
    n.append(na)
    sco.append(int(sc))
    ns.append([na, int(sc)])
ns = sorted(ns, key=itemgetter(1))
if len(ns)==0:
    print("No players")
else:
    for i in range(len(ns)):
        print("%s\t%d"%(ns[len(ns)-i-1][0], ns[len(ns)-i-1][1]), end="\t")
        if i==0:
            print("Gold")
        elif ns[len(ns)-i-1][1]>avg(sco):
            print("Silver")
        else:
            print()