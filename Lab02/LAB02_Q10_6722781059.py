cred = 3+3+1

its100 = float(input("enter grade from ITS100: "))
el171 = float(input("enter grade from EL171: "))
scs183 = float(input("enter grade from SCS183: "))

print("Your GPA is %.2f" % ((its100*3 + el171*3 + scs183)/cred))