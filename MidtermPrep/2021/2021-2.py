a, b = input("Please enter your information: ").split(',')
c=0
if a.isnumeric() and b.isalpha():
    a = int(a)
    name = b
    age = a
elif a.isalpha() and b.isnumeric():
    b = int(b)
    name = a
    age = b
else:
    c=1

if c==0 and 0<=age<=120:
    print("Your name is %s." % name)
    print("Your age is %d." % age)
else:
    print("Please enter your complete information.")