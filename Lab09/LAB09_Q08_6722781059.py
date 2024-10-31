def myRange(FirstVal, UpperBound, StepSize):
    l = []
    n = FirstVal
    while n<UpperBound:
        l.append(n)
        n+=StepSize
    return l

f = int(input("Enter the first number: "))
u = int(input("Enter the upper bound: "))
s = int(input("Enter the step: "))
print("Range =", myRange(f, u, s))