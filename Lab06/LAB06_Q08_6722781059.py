s = input("Enter a string: ")
rev = ""
for i in s:
    if i.isupper():
        rev += i.lower()
    elif i.islower():
        rev += i.upper()
    else:
        rev += i

print("Reverse string output:", rev)