#Request the radius of a circle from the user.Calculate both the area and circumference of the circle using the formulas (Area = π
#r^2 and Circumference = 2 π * r). Print the results.
radius= float(input("enter radius of the circle"))
π = 3.14
area= π*radius*radius
print("area of circle is:",area)
circumference= 2*π*radius
print("Circumference of the circle is:",circumference)