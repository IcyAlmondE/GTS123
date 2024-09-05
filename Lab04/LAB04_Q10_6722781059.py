print("Welcome to Income Tax Computation Program\n")
m = int(input("Please enter your income (THB): "))

if m>=0:
    if m<=15000:
        tax = 0
    elif m<=50000:
        tax = (m-15000)*0.05
    elif m<=100000:
        tax = (m-50000)*0.075 + 35000*0.05
    elif m>100000:
        tax = (m-100000)*0.1 + 50000*0.075 + 35000*0.05

    print("\nTax expense = %.2f" % tax)
    print("Your net income after tax = %.2f" % (m-tax))
else:
    print("\nYou are in debt!")