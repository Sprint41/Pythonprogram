# Create two functions and call one within the other, returning the result.
def square(number):
    return number*number
def multiple_of_square(a,b):
    multiply= a*b
    result= square(multiply)
    return result
x=2
y=4
square_multiple= multiple_of_square(x, y)
print(f"The multiple square of {x} and {y} is {square_multiple}")
