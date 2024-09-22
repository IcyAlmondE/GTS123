n = int(input("Input (Number of customers): "))
co = input("Input (Discount code): ")
if 1<=n<=3:
    pr = 399
elif 4<=n<=6:
    pr = 499
else:
    pr = 599

if co=="CASH":
    dis = 5
elif co=="BIRTHDAY":
    dis = 10
elif co=="COVID":
    dis = 30
else:
    dis = 0

print("%d person x %.2f baht" % (n, pr))
print("A subtotal price is %.2f baht" % (n*pr))
print("On-top discount %d%%" % dis)
print("A total price is %.2f baht" % (n*pr*(1 - dis/100)))