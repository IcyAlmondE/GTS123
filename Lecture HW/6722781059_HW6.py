import numpy as np

def distance(p1, p2):
    return np.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2 + (p1[2]-p2[2])**2)

l = []
c = 1
s = input("P%d: "%c)
while s.lower()!='end':
    try:
        if len(s.split())!=3:
            s = input("P%d: "%c)
            continue

        l.append([float(i) for i in s.split()])
        c+=1
        s = input("P%d: "%c)

    except:
        s = input("P%d: "%c)
        continue

c-=1
if c>=2:
    print("There are %d points in total."%c)
    ld = []
    for i in range(c-1):
        print("P%d -> P%d = %.2f"%(i+1, i+2, distance(l[i], l[i+1])))
        ld.append(distance(l[i], l[i+1]))
    print("Total distance is %.2f units."%sum(ld))
else:
    print("There are fewer than two points. There is no distance output.")