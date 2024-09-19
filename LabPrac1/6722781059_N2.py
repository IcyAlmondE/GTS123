s = input("Input: ")
if len(s)==3:
    s = s.upper()
    if s[0] in ["A", "E", "I", "O", "U"] and s[1] in ["A", "E", "I", "O", "U"] and s[2] in ["A", "E", "I", "O", "U"]:
        print("%c%c%c" % (s[0], s[1], s[2]))
        print("%c%c%c" % (s[0], s[2], s[1]))
        print("%c%c%c" % (s[1], s[0], s[2]))
        print("%c%c%c" % (s[1], s[2], s[0]))
        print("%c%c%c" % (s[2], s[0], s[1]))
        print("%c%c%c" % (s[2], s[1], s[0]))
    else:
        print("Invalid input, valid characters: [\"A\", \"E\", \"I\", \"O\", \"U\"]")
else:
    print("Only three characters are allowed.")