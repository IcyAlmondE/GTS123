p=0
while p==0:
    try:
        n = int(input("Enter an integer (0 to exit): "))
        p=1
    except:
        print("Try again")
odd = 0
even = 0
while n!=0:
    if n%2==0:
        even+=1
    else:
        odd+=1
    p=0
    while p==0:
        try:
            n = int(input("Enter an integer (0 to exit): "))
            p=1
        except:
            print("Try again")

print("----------------------------------")
print("The number of even integers is %d"%even)
print("The number of odd integers is %d"%odd)