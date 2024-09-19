s = input("Input: cleartext=")
k = int(input("Input: k="))
if -256<k<256 and s.islower():
    print("Output: ciphertext= ", end='')
    for i in s:
        print("%c" % chr((ord(i)+k)%256), end='')
else:
    print("Input error")