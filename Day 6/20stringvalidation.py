# Check if a string contains only numeric characters using a built-in method.
user_input=input("Enter a string: ")
if user_input.isdigit():
    print("The string contains only numeric characters")
else:
    print("The string contains non-numeric characters")