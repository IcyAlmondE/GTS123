import numpy as np

def distance(p1, p2):
    return np.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2 + (p1[2]-p2[2])**2)

n = 3
arr = []
for i in range(n):
    alt = input("Input coordinate of P%d: "%(i+1)).split()
    arr.append([float(i) for i in alt])
arr = np.array(arr)

dist = []
for i in range(n):
    for j in range(i, n):
        dist.append(distance(arr[i], arr[j]))
print("Output:\nThe longest distance = %.2f"%max(dist))