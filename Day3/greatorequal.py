# Ask the user to input their score in a test. Compare it to a passing score (e.g., 70) using the greater than or equal to (>=) operator. Print whether
# they passed or not
score= float(input("enter test score:"))
if score>=70:
    print("Passed")
else:
    print("Failed")