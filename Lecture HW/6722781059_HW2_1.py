from math import sqrt, ceil

sta = input("Start number: ")
sto = input("End number: ")
ste = input("Step number: ")

if not sta.isnumeric() or not sto.isnumeric() or not sto.isnumeric():
    print("Input ERROR!!")
else:
    sta, sto, ste = int(sta), int(sto), int(ste)
    prime = []
    if sta>=1 and sto>sta and ste>=1:
        print("Starting from %d and ending at %d with a step of %d, there are a total of %d numbers." % (sta, sto, ste, ((sto-sta)//ste + 1)))
        for i in range(sta, sto+1, ste):
            check = 0
            if i==2 or i==3:
                prime.append(i)
            else:
                for j in range(3, ceil(sqrt(i))+2, 2):
                    if i%j==0:
                        break
                    elif j>sqrt(i):
                        check = 1
                if check==1 and i%2!=0:
                    prime.append(i)
            last = i
        print("Among them, %d are prime." % len(prime))
        print("Numbers: ", end='')
        for i in range(sta, sto+1, ste):
            if i in prime:
                print("%d*" % i, end='')
            else:
                print("%d" % i, end='')
            if i!=last:
                print(", ", end='')
    else:
        print("Input ERROR!!")