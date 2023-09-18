#Take the user's weight (in kilograms) and height (in meters) as input and calculate their Body Mass Index (BMI). Print the BMI value.
user_weight= float(input("Enter user's weight in kilogram's:"))
user_height= float(input("enter user's height in meters:"))
height_square= user_height*user_height
body_mass_index= user_weight/height_square
print("User's Body mass index is:",body_mass_index)