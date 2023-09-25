#Generate and print the multiplication table for a number entered by the user using a for loop.
input1=int(input("Enter the number: "))
for i in range(1,11):
        product= input1*i
        print(input1,"x",i,"=",product)