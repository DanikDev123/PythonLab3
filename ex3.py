import math

radius = 6371.01

x1, y1 = map(float, input("Enter point 1 (latitude and longitude) in degrees: ").split(",")) #можно использовать в случае, если вводится несколько чисел через разделитель (в данном случае через запятую)
x2, y2 = map(float, input("Enter point 2 (latitude and longitude) in degrees: ").split(","))

x1 = math.radians(x1)
y1 = math.radians(y1)
x2 = math.radians(x2)
y2 = math.radians(y2)

d = radius*math.acos((math.sin(x1)) * math.sin(x2) + math.cos(x1) * math.cos(x2)*math.cos(y1-y2))
print(f"The distance between the two points is {d:.2f} km")