import math

prime=[2]
for i in range(3, 1000001, 2):
    for j in range(len(prime)):
        if i%prime[j] ==0:
            break
        if prime[j]>math.sqrt(i):
            prime.append(i)
            break

num = int(input("Prime No."))
print(prime[num-1])

# print(prime)