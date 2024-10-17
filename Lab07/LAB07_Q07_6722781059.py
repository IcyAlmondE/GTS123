print("===================\nCashier Program\n===================\n")

l = []

p=0
try:
    p = float(input("Enter item price or -1 when finished: "))
except:
    print("Input should be a number")
while p!=-1:
    if p!=0:
        l.append(p)
    try:
        p = float(input("Enter item price or -1 when finished: "))
    except:
        print("Input should be a number")
        p=0

print("\nTotal purchase amount is %.2f\n" % sum(l))
ch=0
while ch==0:
    try:
        n = float(input("Your payment: "))
        ch = 1
    except:
        print("Input should be a number")

print("\nYou bought %d items today." % len(l))
print("Your change is %.2f baht." % (n-sum(l)))