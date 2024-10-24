s = input("Input a sentence: ").split()
d = {}
for i in s:
    i = i.strip(',').strip('.')
    if i not in d:
        d[i] = 1
    else:
        d[i] += 1
no = True
print("Output:")
for i in d.keys():
    if d[i]>1:
        print(i.lower())
        no = False
if no:
    print("none")