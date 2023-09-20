#  Write a program that asks the user for their age and height (in centimeters). Use the and operator to check if they are both older than 18 and
# taller than 160 cm. Print whether they meet both conditions.
age= int(input("enter age:"))
height= float(input("enter height in centimeters:"))
if age>18 and height>160:
    print("They meet the conditions")
else:
    print("They don't meet the conditions.")