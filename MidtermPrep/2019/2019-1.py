hr, min, sec = input("Input: ").split(":")
hr, min, sec = int(hr), int(min), int(sec)
if 0<=hr<=23 and 0<=min<=60 and 0<=sec<=60:
    print("The number of seconds =", hr*3600+min*60+sec)
else:
    print("Invalid time")