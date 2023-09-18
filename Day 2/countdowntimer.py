#Request a number from the user and use a loop to count down from that number to 1, printing each number.
try:
    number = int(input("enter a number:"))
    if number <=0:
        print("please enter a positive integer.")
    else:
        print("Counting down:")
        while number>=1:
            print(number)
            number-=1
except ValueError:
    print("Invalid input. Please enter a valid number.")
