s = input("Input: Enter a word:")
l = []
while s!='exit':
    if s[-1]=='y':
        l.append(s[:-1]+'ily')
    else:
        l.append(s)

    s = input("Input: Enter a word:")

print("Output:", l)