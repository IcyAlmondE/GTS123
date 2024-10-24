from operator import itemgetter
s = input("Input (DONE = exit): ")
d = {}
while s!="DONE":
    try:
        id, sc = s.split()
        if id in d:
            print("Duplicated ID")
        elif (not id.isnumeric()) or (not sc.isnumeric()) or int(id)<1 or int(sc)<1:
            print("Invalid Input")
        else:
            d[id] = sc
    except:
        print("Invalid Input")
    s = input("Input (DONE = exit): ")
ds = sorted(d.items(), key=itemgetter(1), reverse=True)
print("Output:")
for i in ds:
    print(i[0], i[1])