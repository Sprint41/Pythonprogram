# Ask the user for their exam score. Use an if-else statement to check if they passed (scored 50 or higher) or failed (scored below 50). Print the result.
user_score= float(input("Enter user score:"))
if user_score>=50:
    print("User is passed")
else:
    print("User has failed")