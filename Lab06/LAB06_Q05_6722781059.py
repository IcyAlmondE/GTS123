gp = [[], [], []]

n = int(input("how many persons in a group? : "))

gr = ['A', 'B', 'C']
for i in range(3):
    print("\nplease enter grade from group %c"%gr[i])
    for j in range(n):
        sc = float(input("enter grade: "))
        gp[i].append(sc)
print()
for i in range(3):
    print("the highest grade of group %c is %.1f" % (gr[i], max(gp[i])))