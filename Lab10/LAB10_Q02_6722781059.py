import numpy as np

arr = np.zeros([3, 4])
for i in range(3):
    for j in range(4):
        arr[i][j] = int(input("Input C%d: "%(4*i+j+1)))

try:
    sol = np.matmul(np.linalg.inv(arr[:, :3]), arr[:, 3])
    print("\nSolution:")
    print("x = %.2f"%sol[0])
    print("y = %.2f"%sol[1])
    print("z = %.2f"%sol[2])
except:
    print("Unable to find a solution")