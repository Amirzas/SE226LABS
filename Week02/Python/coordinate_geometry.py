import math
x1 = float(input("Enter x1: \n"))
y1 = float(input("Enter y1: \n"))
x2 = float(input("Enter x2: \n"))
y2 = float(input("Enter y2: \n"))
distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print(f"The distance between the two points is {distance}")