#  Determine if a string is all uppercase or all lowercase.
user_input=input("Enter a string:")
if user_input.isupper()==True:
    print("The given input contains all uppercase.")
elif user_input.islower()==True:
    print("The given input contains all lowercase.")
else:
    print("The given input contains the mixture of both the cases.")