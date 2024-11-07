import numpy as np

data = np.loadtxt("sales.tsv", delimiter='\t', dtype=int)

# print(data)

sumbr = np.sum((data[:,1:]), axis=1)
sortbr = np.argsort(sumbr)
for i in range(len(data)):
    j = len(data)-i-1
    print(data[sortbr[j]][0], "\t%d"%sumbr[sortbr[j]])