d = {'1':0, '2':0, '5':0, '10':0}
sm = 0
print("Welcome to coin deposit machine")
while 1:
    s = input("Please insert coin: ")
    if s=='done':
        break
    if s not in d:
        print("Only 1,2,5 and 10 baht coin are allowed")
        continue
    print("You inserted %s baht coin"%s)
    d[s]+=1
    sm+=int(s)
    print("Current Balance: %d baht"%sm)
print("<-----Deposit Summary----->")
for i in d:
    print("%s baht coins -> %d"%(i, d[i]))
print("Deposit Amount: %d baht"%sm)