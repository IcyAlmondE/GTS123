namelist = ["Satawat", "Pisit", "Thanaphong", "Pished", "Nut", "Amon"]

print("Studen list:", namelist)
name = input("Please enter a student's name that you want to delete (q = exit): ")
while name!='q':
    if name in namelist:
        print("You will remove \' %s \' from this class."%name)
        yn = input("Please type (Confirm 'y', Cancel 'n'): ")
        if yn.lower() == 'y':
            namelist.remove(name)
            # namelist.pop(namelist.index(name))
    else:
        print("There is no %s in this class." % name)
    print("\nStuden list:", namelist)
    name = input("Please enter a student's name that you want to delete (q = exit): ")