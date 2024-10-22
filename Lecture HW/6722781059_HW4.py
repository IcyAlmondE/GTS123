l = []
ch = 0
while sum(l)<=1000:
    n = input("Numbers: ")
    if n=='EXIT':
        ch = 1
        break
    else:
        try:
            n = float(n)
            l.append(n)
        except:
            continue
if ch==1:
    print("Exit without summary.")
else:
    print("----------")
    l = sorted(l)
    print("%.2f"%l[0], end='')
    for i in range(1, len(l)):
        print(", %.2f"% l[i], end='')
    print("\nsum = %.2f"% sum(l))