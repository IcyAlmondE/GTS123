s = input("Input: Enter a word:")
l = []
while s!='exit':
    l.append(s.capitalize())
    s = input("Input: Enter a word:")
print("Output:", l)