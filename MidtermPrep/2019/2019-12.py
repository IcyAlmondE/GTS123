c1 = input("Give me a character: ")
c2 = input("Give me another character: ")
print("Output:")
if c1.isalpha() and c2.isalpha():
    if c1>c2:
        start = c2
        end = c1
    else:
        start = c1
        end = c2
    s = 'abcdefghijklmnopqrstuvwxyz'
    for i in range(s.index(start), s.index(end)+1):
        print(s[i], end='')
else:
    print("You need to input two characters.")