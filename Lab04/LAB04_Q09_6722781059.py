m = int(input("Input parking time (in minutes) : "))
pr = (m//60)*20

if m%60 > 15:
    pr+=20

print("The charge is %d baht." % pr)