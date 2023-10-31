# Use a return statement to exit a function early if a certain condition is met.
def div(a,b):
    if b==0:
        return f"error: divisible by zero."
    result= a/b
    return result
x=5
y=0
div_result=div(x,y)
print(f"The divison of {x} with {y} is {div_result}")