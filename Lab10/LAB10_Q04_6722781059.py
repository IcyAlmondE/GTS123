import numpy as np

data = np.loadtxt("sales.tsv", delimiter='\t', dtype=int)
sumbr = np.zeros(len(data))

# print(data)

for i in range(len(data)):
    sumbr[i] = sum((data[i][1:]))

sortbr = np.argsort(sumbr)
for i in range(len(sumbr)):
    j = len(sumbr)-i-1
    print(data[sortbr[j]][0], "\t%d"%sumbr[sortbr[j]])