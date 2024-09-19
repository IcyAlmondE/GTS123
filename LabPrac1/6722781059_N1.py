km = input("Enter your running pace (minutes per kilometer): ")
s = input("Enter your distance (a) Mini-marathon, (b) Half-marathon, (c) Full-marathon: ")
s = s.lower()
min, sec = km.split(":")
min, sec = int(min), int(sec)
sec+=min*60
if s=="a":
    fin = sec*10
    hrfin = fin//3600
    minfin = (fin%3600)/60
    print("Your estimated finish time is %d hours %d minutes" % (hrfin, minfin))
    if fin<=9000:
        print("You can finish in cutoff time (Your cutoff time is 2.50 hours).")
    else:
        print("You cannot finish in cutoff time (Your cutoff time is 2.50 hours).")
elif s=="b":
    fin = sec*21.0975
    hrfin = fin//3600
    minfin = (fin%3600)/60
    print("Your estimated finish time is %d hours %d minutes" % (hrfin, minfin))
    if fin<=14400:
        print("You can finish in cutoff time (Your cutoff time is 4.00 hours).")
    else:
        print("You cannot finish in cutoff time (Your cutoff time is 4.00 hours).")
elif s=="c":
    fin = sec*42.195
    hrfin = fin//3600
    minfin = (fin%3600)/60
    print("Your estimated finish time is %d hours %d minutes" % (hrfin, minfin))
    if fin<=21600:
        print("You can finish in cutoff time (Your cutoff time is 6.00 hours).")
    else:
        print("You cannot finish in cutoff time (Your cutoff time is 6.00 hours).")
else:
    print("Invalid distance selection")