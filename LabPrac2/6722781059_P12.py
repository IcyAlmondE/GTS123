id, idsc = [], []
while 1:
    s = input("Enter student ID and score: ")
    if s=='done 0':
        break
    ii, ss = s.split()
    if not ii.isnumeric() or len(ii)!=4:
        print("Invalid ID format!")
        continue
    if int(ii) in id:
        print("The ID is already recorded!")
        continue
    if int(ss)<0 or int(ss)>100:
        print("Invalid score!")
        continue
    ii, ss = int(ii), int(ss)
    id.append(ii)
    idsc.append([ii, ss])
print("List: ")
if len(idsc)==0:
    print("> no score is recorded!")
else:
    idsc = sorted(idsc)
    for i in range(len(idsc)):
        print("%d %d"%(idsc[i][0], idsc[i][1]))
        sc = [i[1] for i in idsc]
    print("There are %d student(s). The average score is %.2f points."%(len(idsc), (sum(sc)/len(sc))))