def UserInput():
    ww = float(input("Input your weight (kilogram): "))
    hh = float(input("Input your height (meter): "))
    return [ww, hh]

def FindBMI(ww, hh):
    return ww/(hh*hh)

def ShowBMI(MyBMI):
    print("The user BMI is %.2f"%MyBMI)

UserBMI = UserInput()
ShowBMI(FindBMI(UserBMI[0], UserBMI[1]))