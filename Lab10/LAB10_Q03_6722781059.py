import numpy as np

data = np.loadtxt("grades.tsv", delimiter='\t', dtype=str)
cre = [3, 2, 1, 3, 3, 3]
# print(data)
gpa = np.zeros(len(data))

for i in range(len(data)):
    for j in range(len(cre)):
        gpa[i] += float(data[i][j+1])*cre[j]
    gpa[i] /= sum(cre)

print("Student ID\tGPA")
for i in range(len(data)):
    print(data[i][0], "\t%.2f"%gpa[i])