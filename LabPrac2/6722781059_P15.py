from operator import itemgetter

d = {'ce':0, 'che':0, 'ec':0, 'ie':0, 'me':0}
data = []
while 1:
    s = input("Input: ")
    if s=='done':
        break
    na, ma, gr = s.split()
    gr = float(gr)
    if ma not in d or gr<0 or gr>4:
        print("ERROR")
        continue
    d[ma]+=1
    data.append([na, ma, gr])
print("----SUMMARY----")
for i in d:
    print("%s = %d"%(i, d[i]))
print("----LIST----")
data = sorted(data, key=itemgetter(2))
if len(data)==0:
    print("The list is empty")
else:
    for i in range(len(data)):
        ind = len(data)-i-1
        print("%s %s %.2f"%(data[ind][0], data[ind][1], data[ind][2]))