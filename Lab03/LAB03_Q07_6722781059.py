import random as r

n1 = r.choice([9, 8])
n2 = r.choice([7, 6])
n3 = r.choice([5, 4])
n4 = r.choice([3, 2])
n5 = r.choice([1, 0])

#print(type(n1))
print("Your OTP is %d%d%d%d%d. This password will be expired within 5 minutes." % (n1, n2, n3, n4, n5))