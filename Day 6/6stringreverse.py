# Reverse a string without using any built-in functions.
city_name="kolkata"
reversed_string=""
for char in city_name[::-1]:
    reversed_string+= char
print("Reversed String is:",reversed_string)