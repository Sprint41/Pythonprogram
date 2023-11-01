# Define a recursive function that returns the factorial of a number.
def factorial(number):
    if number==0:
        return 1
    else:
        return number*factorial(number-1)
number=5
fact_result=factorial(number)
print("The factorial of",number,"is:",fact_result)