import random as r

li = []
for i in range(4):
    li.append(input("Enter string#%d: "%(i+1)))

r.shuffle(li)
print("\nRandom order of the sentence: ", end='')
for i in range(4):
    print(li[i], end=' ')