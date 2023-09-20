# Create a program that asks the user for their age and whether they have a student ID. Use nested if-else statements to determine the ticket price based
# on age and student status. Print the ticket price.
age= int(input("Enter user age:"))
student_id= input("Enter student ID:")
if 0<age<=16:
    print("The price is 100")
elif 16<age<=18:
        print("The price is 150")
elif age>18:
        print("The price is 200")
else:
       print("Invalid input. Please enter valid input.")