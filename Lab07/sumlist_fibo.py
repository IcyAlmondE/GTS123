n = int(input())

fb = [1, 1]
for i in range(2, n):
    fb.append(fb[i-2]+fb[i-1])

print(fb[n-1])