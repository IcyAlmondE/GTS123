h = input("Height: ")
if h.isnumeric():
    h = int(h)
    if h>0:
        for i in range(h):
            print("#"*(h-(i+1)), end='')
            print("."*(2*i+1), end='')
            print("#"*(h-(i+1)))
    else:
        print("Error")
else:
    print("Error")