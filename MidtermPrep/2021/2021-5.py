a, b, c = input("a, b, c = ").split()
bo = ['True', 'False']
if a in bo and b in bo and c in bo:
    if (a=='False' and b=='False' and c=='False') or a=='True':
        print("Grant")
    else:
        print("Deny")
else:
    print("Invalid input")