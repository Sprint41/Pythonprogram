# Ask the user to input a character (letter, digit, or special character). Use nested if-else statements to classify it as a letter, digit, or special
# character. Print the classification.
input= input("enter the input:")
if input.isdigit():
    print("The given input is digit")
elif input.isalpha():
    print("The given input is letter")
else:
    print("The given input is special character")
