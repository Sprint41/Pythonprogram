#  Write a program to check if a given string is a palindrome (reads the same forwards and backwards).
user_input=input("enter a string: ")
constring= user_input.replace(" ", "").lower()
reversed_string= constring[::-1]
if constring==reversed_string:
    print("The String is palindrome")
else:
    print("The string is not a palindrome")