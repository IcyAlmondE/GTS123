num = int(input("Enter a four-digit integer: "))
n1 = num//100
n2 = num%100

print("The result of %d + %d = %d" % (n1, n2, n1+n2))
print("The result of %d - %d = %d" % (n1, n2, n1-n2))
print("The integer value of %d/%d = %d" % (n1, n2, n1//n2))
print("The remainder of %d/%d = %d" % (n1, n2, n1%n2))