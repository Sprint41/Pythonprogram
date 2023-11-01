# Call a function within an expression and use its return value in a calculation.
def square(num):
    return num*num
def sum_square(a,b):
    total= a+b
    result= square(total)
    return result
x=3
y=5
square_sum=sum_square(x,y)
print (f"The square of the sum of {x} and {y} is: {square_sum}")

