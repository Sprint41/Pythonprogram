# Ask the user for their test score. Use if-elif-else statements to assign a letter grade (A, B, C, D, or F) based on score ranges. Print the letter grade.
user_score= int(input("Enter the score:"))
if 90<user_score<=100:
    print("Grade is A")
elif 80<user_score<=90:
    print("Grade is B")
elif 70<user_score<=80:
    print("Grade is C")
elif 60<user_score<=70:
    print("Grade is D")
elif 50<user_score<=60:
    print("Grade is E")
elif 40<user_score<=50:
    print("Grade is F")
elif 0<=user_score<=40:
    print("Fail")
else:
    print("Invalid input.Please enter valid input.")
