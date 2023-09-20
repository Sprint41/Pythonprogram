# Ask the user to create a password. Check if the password is at least 8 characters long and contains at least one uppercase letter using
# comparison operators and logical AND. Print whether it's a strong password.
user_password = input("Please create a password: ")
if len(user_password) >= 8 and any(char.isupper() for char in user_password):
    print("Congratulations! It's a strong password.")
else:
    print("Your password is not strong enough.")

