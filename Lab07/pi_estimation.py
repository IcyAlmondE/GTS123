import random as r

n = 10000000
p = 0
for i in range(n):
    x = r.uniform(-1, 1)
    y = r.uniform(-1, 1)
    if x**2+y**2<=1:
        p+=1

print((p/n)*4)