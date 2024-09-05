m = int(input("Enter money you have: "))
p = int(input("Enter price of item: "))

print("Tax: %.2f" % (p*0.08))
total = p*1.08
print("Total price: %.2f" % total)

if m>total : 
    print("yes you have enough money to buy")
else:
    print("You have shortfall of %.2f, you cannot buy." % (total-m))