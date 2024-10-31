def CelsiusToFarenheit(c):
    return (1.8*c)+32

c = float(input("Input temperature in degree Celcius: "))
print("The degree in Farenheit is %.2f"%CelsiusToFarenheit(c))