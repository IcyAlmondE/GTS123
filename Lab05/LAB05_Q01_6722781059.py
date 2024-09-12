even = 0
odd = 0

for i in range(5):
    x = input("enter a number ")
    if x.isnumeric() and int(x)%2==0:
        even+=1
    elif x.isnumeric():
        odd+=1

print("there were %d even numbers" % even)
print("there were %d odd numbers" % odd)