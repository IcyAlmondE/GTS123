print("===== MAIN MENU =====")
print("1. Addition\n2. Subtraction\n3. Exit\n")
op = input("Select an operation (1-3): ")

while op not in "123":
    print("Try again")
    op = input("Select an operation (1-3): ")

while op!='3':
    try:
        a, b = input("Enter two numbers: ").split()
        a, b = int(a), int(b)
        if op=='1':
            print("%d + %d = %d" % (a, b, a+b))
        elif op=='2':
            print("%d - %d = %d" % (a, b, a-b))
    except:
        print("Try again")
    
    print("\n===== MAIN MENU =====")
    print("1. Addition\n2. Subtraction\n3. Exit\n")
    op = input("Select an operation (1-3): ")

print("Bye!!!")