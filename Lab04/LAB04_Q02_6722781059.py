print("Fever Symptoms Advisor Program")
temp = float(input("Check your body temperature in F = "))
if temp>=100.4:
    print("You got a fever.")
    tre = input("Choose your treatment : 1 = medication 2 = no medication >>> ")

    if tre=="1":
        print("Take Tylenol every 4 hours as needed")
    elif tre=="2":
        print("Taking a bath in lukewarm water or get the cool packs")
    else:
        print("You choose the wrong choice")
else:
    print("You are fine.")