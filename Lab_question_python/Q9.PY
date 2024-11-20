
x1 = int(input("Enter x-coordinate of point 1: "))
y1 = int(input("Enter y-coordinate of point 1: "))
x2 = int(input("Enter x-coordinate of point 2: "))
y2 = int(input("Enter y-coordinate of point 2: "))
x3 = int(input("Enter x-coordinate of point 3: "))
y3 = int(input("Enter y-coordinate of point 3: "))


if (x2 - x1) * (y3 - y1) == (y2 - y1) * (x3 - x1):
    print("The points are collinear (they lie on a straight line).")
else:
    print("The points are not collinear.")