p = float(input("Enter the price of the product: "))
n = int(input("Enter the number of items: "))
total = p*n
pro = input("Do you have a promotion code (y/n)? ")
pro = pro.upper()
if pro=="Y":
    code = input("Enter your promotion code: ")
    code = code.upper()
    print("----------------------------")
    if code=="SUPERSALE1010":
        dis = total*0.7
    elif code=="MAGA1010":
        dis = total*0.8
    elif code=="LOVESHOPPING":
        dis = total*0.9
    else:
        print("Your promotion code is invalid.\n----------------------------")
        dis = 0
    if dis!=0:
        print("Total Amount: %.2f baht" % total)
        print("Amount after Discount: %.2f baht" % dis)
    else:
        print("Total Amount: %.2f baht" % total)
elif pro=="N":
    print("----------------------------")
    print("Total Amount: %.2f baht" % total)
else:
    print("Input error")