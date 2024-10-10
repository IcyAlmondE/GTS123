li = input("Enter a comma-separated list: ").split(',')

for i in range(len(li)):
    for j in range(len(li)):
        for k in range(len(li)):
            if i<j and j<k:
                print(li[i], li[j], li[k])