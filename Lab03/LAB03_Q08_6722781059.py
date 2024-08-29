s = input("Input a word: ")
print("The input word is \"%s\"" % s)

print("1. %s" % s.strip().upper())
print("2. %s" % s.strip().capitalize())
print("3. %s" % str(s.isnumeric()))
print("4. %s" % str(s.isalpha()))
print("5. %s" % str(s.isupper()))