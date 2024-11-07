import numpy as np

data = np.loadtxt("grades.tsv", delimiter='\t', dtype=str)
cre = [3, 2, 1, 3, 3, 3]
# print(data)

ids = data[:, 0]
g = data[:, 1:].astype(float)
g = np.sum(g*np.array(cre), axis=1)/sum(cre)

print("Student ID\tGPA")
for i in range(len(data)):
    print(ids[i], "\t%.2f"%g[i])