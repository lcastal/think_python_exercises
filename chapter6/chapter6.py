import math

def hypotenuse(a, b):
    dsquared = a**2 + b**2
    i = math.sqrt(dsquared)
    return i

def distance(x1, y1, x2, y2):
    dx = x1 - x2
    dy = y1 - y2
    dsquared = dx**2 + dy**2
    distance = math.sqrt(dsquared)
    return distance

def area(radius):
    a = math.pi * radius**2
    return a

def circle_area(xc, yc, xp, yp):
    radius = distance(xc, yc, xp, yp)
    result = area(radius)
    return result


a = input("lato a: ")
b = input("lato b: ")
hyp = hypotenuse(float(a), float(b))

print("ipotenusa: %f" % hyp)

print("coordinate centro")
xc = int(input("xc: "))
yc = int(input("yc: "))

print("punto circonferenza")
xp = int(input("xp: "))
yp = int(input("yp: "))

area = circle_area(xc, yc, xp, yp)

print("area cerchio: %f" % area)
