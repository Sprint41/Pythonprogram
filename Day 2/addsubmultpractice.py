#Write a program that takes two numbers as input and calculates their sum. Print the result.
num1 = int(input("enter first number:"))
num2 = int(input("enter second number:"))
addition = num1+num2
print("addition of two numbers:",addition)

#Create a program that prompts the user for two numbers and calculates their difference. Display the result.
difference= num1 - num2
print("Difference of two numbers:",difference)

#Ask the user to enter a number and then print the multiplication table for that number from 1 to 10.
integer = int(input("Enter a number:"))
print("Multiplication table of",integer,"is:")
for i in range(1,11):
    print(integer*i)
