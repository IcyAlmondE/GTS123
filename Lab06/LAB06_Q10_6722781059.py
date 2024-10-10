lfr = input("List of fruits: ")
lfr = lfr.strip('[').strip(']').split(',')

fr = []
for i in lfr:
    fr.append(i.strip().strip("\'"))

#fr = ['Apple', 'Banana', 'Orange', 'Grape', 'Mango', 'Kiwi']
nfr = []

for i in fr:
    nfr.append(len(i))

#print("List of fruits:", fr)
for i in range(len(fr)):
    if nfr[i]>=6:
        print("%s is 6 characters or more!" % fr[i])
    else:
        print("%s is only %d long!" % (fr[i], nfr[i]))