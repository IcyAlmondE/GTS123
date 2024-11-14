d = {'JPY':0.29, 'USD':31.99, 'EUR':35.62}
l = []
while 1:
    s = input("Input: ")
    if s=='end':
        break
    cur, val = s.split()
    if cur not in d or float(val)<1:
        print("ERROR")
        continue
    l.append([cur, float(val)])
if len(l)!=0:
    for i in l:
        print("%.2f %s is %.2f THB"%(i[1], i[0], (i[1]*d[i[0]])))