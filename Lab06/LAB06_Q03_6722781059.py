print("="*24)

li = []
for i in range(5):
    n = int(input("Input#%d: "%(i+1)))
    li.append(n)

op = input("Select the option: 1)Summary,2)average,3)min,4)max ....")
if op=='1':
    print("Your result is %d"%sum(li))
elif op=='2':
    print("Your result is %d"%(sum(li)/5))
elif op=='3':
    print("Your result is %d"%min(li))
elif op=='4':
    print("Your result is %d"%max(li))