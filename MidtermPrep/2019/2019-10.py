s = input("DNA: ")
if s.isalpha():
    b = input("Base: ")
    if b.isalpha():
        c = 0
        for i in s:
            if i==b:
                print("c: %c" % i)
                print("True if test")
                c+=1
            else:
                print("c: %c" % i)
        print("There are %d times that the base %c occur in this DNA." % (c, b))
    else:
        print("This is not DNA String")
else:
    print("This is not DNA String")