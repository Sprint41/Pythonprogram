#Prompt the user to enter a letter. Use an if statement to determine if it's a vowel (a, e, i, o, u) or a consonant. Print the result.
user_letter=(input("Enter a letter:"))
if user_letter in 'aeiou':
    print("The entered input is a vowel")
elif user_letter in 'bcdfghjklmnpqrstvwxyz':
    print("The entered letter is a consonant")
else:
    print("Invalid input. Please enter a valid input.")