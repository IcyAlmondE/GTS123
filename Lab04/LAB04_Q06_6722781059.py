x1, y1 = 0.0, 0.0
x2, y2 = 2.0, 0.0
x3, y3 = 1.0, 2.0

x = float(input("Input x = "))
y = float(input("Input y = "))

a = ((y2-y3)*(x-x3) + (x3-x2)*(y-y3))/((y2-y3)*(x1-x3) + (x3-x2)*(y1-y3))
b = ((y3-y1)*(x-x3) + (x1-x3)*(y-y3))/((y2-y3)*(x1-x3) + (x3-x2)*(y1-y3))
g = 1-a-b

if a>0 and b>0 and g>0:
    print("Point (x,y) inside polygon")
else:
    print("Point (x,y) outside polygon")