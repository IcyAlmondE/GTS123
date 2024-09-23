b, d, a = input("Input: borrowed amount, duration(years), annual interest(%) ").split()
b, d, a = int(b), int(d), int(a)
for i in range(1, d):
    b = b*(1+a/100)
    p = int(input("Input: pay at the end of year %d " % i))
    b-=p
    if b<0:
        print("Output: You already clear your loan")
        break
b = b*(1+a/100)
if b>0:
    print("Output: To clear your loan, you need to repay", b, "at the end of year %d" % (d))
