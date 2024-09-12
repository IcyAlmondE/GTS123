total = 0
l, s, h = 0, 0, 0
for i in range(10):
    st = input("Feeling Like (\"L\"), Sad (\"S\"), and Heart (\"H\")? ")
    if st not in ["L", "S", "H"]:
        print("Invalid input, accepts only (L/S/H).")
    elif st=="L":
        l+=1
        total+=1
    elif st=="S":
        s+=1
        total+=1
    elif st=="H":
        h+=1
        total+=1

print("============")
print("Total is", total)
print("============")
lp = float(l*100/total)
sp = float(s*100/total)
hp = float(h*100/total)
print("Like: %d (%.2f%%)" % (l, lp))
print("Sad: %d (%.2f%%)" % (s, sp))
print("Heart: %d (%.2f%%)" % (h, hp))