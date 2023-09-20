# Request the lengths of three sides of a triangle from the user. Use nested if-else statements to determine if it's equilateral (all sides equal), isosceles (two
#sides equal), or scalene (all sides different). Print the result.
len1= float(input("Enter length of first side:"))
len2= float(input("Enter length of second side:"))
len3= float(input("Enter length of third side:"))
if len1==len2==len3:
     print("The triangle is equilateral triangle")
elif len1==len2!=len3 or len1==len3!=len2 or len2==len3!=len1:
    print("The triangle is isosceles triangle")
else:
     print("The triangle is scalene")