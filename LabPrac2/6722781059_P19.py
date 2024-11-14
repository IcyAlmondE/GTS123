d = {}
while 1:
    s = input("Input: ")
    if s=='done':
        break
    s = s.split()
    if s[0] not in d:
        d[s[0]] = int(s[1])
    else:
        d[s[0]]+= int(s[1])

if len(d)==0:
    print("Empty List")
print("###Summary###")
for i in d:
    print("Total Number of %s : %d"%(i, d[i]))