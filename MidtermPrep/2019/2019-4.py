import random as r

w = int(input("Rectangle width: "))
h = int(input("Rectangle height: "))
t = int(input("Border thickness: "))

for i in range(h):
    for j in range(w):
        if i<t or i>h-t-1 or j<t or j>w-t-1:
            print(r.choice(['#', '*', '$']), end='')
        else:
            print(' ', end='')
    print()