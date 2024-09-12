print("Menu:\n===============")
print("A - Americano (50)\nE - Espresso (40)\nG - Green tea (60)")
print("===============\n")

s = input("Input: ")

num = 0
price = 0
for i in s:
    if i=='A':
        num+=1
        print("%d. Americano 50" % num)
        price+=50
    elif i=='E':
        num+=1
        print("%d. Espresso 40" % num)
        price+=40
    elif i=='G':
        num+=1
        print("%d. Green tea 60" % num)
        price+=60
print("===============")
print("Quantity: %d" % num)
print("Vat: %.2f" % (0.07*price))
print("Total: %.2f" % price)
print("Grand total: %.2f" % (1.07*price))