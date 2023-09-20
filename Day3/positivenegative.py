#Write a program that asks the user for a number and uses an if statement to check if it's positive or negative. Print the result.
user_num= float(input("Enter an integer:"))
if user_num<0:
    print("The entered number is negative")
if user_num>0:
    print("The entered number is positive")
if user_num==0:
    print("The number is zero")
