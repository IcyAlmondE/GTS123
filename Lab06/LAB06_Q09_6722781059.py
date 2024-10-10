la = input("a=")
lb = input("b=")

a = la.strip('[').strip(']').split(',')
b = lb.strip('[').strip(']').split(',')

a = [int(x.strip()) for x in a]#[1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [int(x.strip()) for x in b]#[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

dupe = []
a, b = sorted(a), sorted(b)

for i in range(len(a)):
    if a[i]==a[i-1]:
        continue
    for j in range(len(b)):
        if b[j]==b[j-1]:
            continue
        if b[j]==a[i]:
            dupe.append(b[j])
            break
print(dupe)