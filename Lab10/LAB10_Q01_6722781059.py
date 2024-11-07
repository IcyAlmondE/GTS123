import numpy as np

def arrnopoint(arr):
    print('[[', end='')
    for i in range(len(arr)):
        for j in range(len(arr)):
            if j!=len(arr)-1:
                print(int(arr[i][j]), end=' ')
            else:
                print(int(arr[i][j]), end=']')
        if i!=len(arr)-1:
            print()
            print(' [', end='')
        else:
            print(']')   

n = int(input("Input size of matrix: "))
arr = np.zeros([n, n])
for i in range(n):
    for j in range(n):
        arr[i][j] = int(input("Input element at row %d column %d: "%(i+1, j+1)))
print("\nOutput:")
print("Matrix =")
arrnopoint(arr)
det = np.linalg.det(arr)
print("Determinant =", det)
if det!=0:
    print("Inverse matrix =")
    print(np.linalg.inv(arr))