s = input("Enter a line (or \'END\' to finish): ")
d = {}
while s.lower()!='end':
    for i in s.lower().split():
        i = i.strip(',').strip('.')
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    s = input("Enter a line (or \'END\' to finish): ")
dc = [0, 0, 0]
for i in d.values():
    if i==1 or i==2:
        dc[0]+=1
    elif i==3 or i==4:
        dc[1]+=1
    else:
        dc[2]+=1
print("1. Number of words that appear once or twice:", dc[0])
print("2. Number of words that appear three and four times:", dc[1])
print("3. Number of words that appear more than four times:", dc[2])