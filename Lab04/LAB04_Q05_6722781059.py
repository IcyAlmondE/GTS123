n = int(input("Please specify amount of money you would like to withdraw:"))

b500 = n//500
n = n%500
b100 = n//100
n = n%100
b50 = n//50
n = n % 50
c2 = n//2
n = n%2
c1 = n

print("we may give you:")
print("%d bill(s) of 500 baht" % b500)
print("%d bill(s) of 100 baht" % b100)
print("%d bill(s) of 50 baht" % b50)
print("%d coin(s) of 2 baht" % c2)
print("%d coin(s) of 1 baht" % c1)