s1 = input("Input sequence1: ").split()
s2 = input("Input sequence2: ").split()
ss1, ss2 = set(), set()
for i in s1:
    if i.isnumeric():
        ss1.add(i)
for i in s2:
    if i.isnumeric():
        ss2.add(i)
if len(ss1&ss2)>0:
    print("Output: True")
else:
    print("Output: False")