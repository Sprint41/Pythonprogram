# Write a function to calculate the factorial of a number and call it multiple times.
def num_factorial(number):
    if number==0:
        return 1
    else:
        result= 1
        for i in range(1, number+1):
            result*= i
        return result
factorial= num_factorial(5)
print("Factorial of 5 is:",factorial)
factorial2= num_factorial(0)
print("Factorial of 0 is:",factorial2)
