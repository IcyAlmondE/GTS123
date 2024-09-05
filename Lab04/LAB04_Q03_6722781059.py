day = int(input("Input the number of days: "))
hour = int(input("Input the number of hours: "))

print("Please select a choice:\n1-to calculate the total number of seconds or\n2-to calculate the total number of minutes:")
ch = input("Enter your selected choice: ")
print("------------------------------------------------")

if ch=="2":
    print("The total number of minutes are %d." % (day*24*60 + hour*60))
elif ch=="1":
    print("The total number of seconds are %d." % (day*24*3600 + hour*3600))