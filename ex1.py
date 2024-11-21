
import math 
radius = float(input("Enter length: "))
side  = 2*radius*math.sin(math.pi/5)
area = round((3*math.sqrt(3)*(side**2))/2 ,2)

print (f"The area of the pentagon is: {area}")
