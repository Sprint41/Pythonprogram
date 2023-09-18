input_1= float(input("enter the first input:"))
input_2= float(input("enter the second input:"))
print("Choose an operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
choice= input("Enter your choice (1/2/3/4): ")
if choice == '1':
    result= input_1+input_2
    operation= "addition"
elif choice == '2':
    result = input_1 - input_2
    operation= "subtraction"
elif choice =='3':
    result= input_1*input_2
    operation= "multiplication"
elif choice =='4':
    result= input_1/input_2
    operation= "division"
else:
    result= "Invalid Input"
    operation= "Invalid Operation"

print("Result of",operation,"is",result)


