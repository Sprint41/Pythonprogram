#Request a number from the user and compare it to a specific range (e.g., 1 to 100) using the greater than, less than, and logical AND operators.
# Print whether the number is within the range.
user_number = int(input("Please enter a number: "))

if user_number > 1 and user_number < 100:
    print("The number",user_number,"is within the range to 100.")
else:
    print(f"The number",user_number,"is NOT within the range 1 to 100.")
