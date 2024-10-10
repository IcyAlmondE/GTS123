li = input("Enter a comma-separated list: ").split(',')

for i in li:
    for j in li:
        for k in li:
            if(i!=j and i!=k and j!=k):
                print(i, j, k)