# Create a function that returns "Even" if a given number is even and "Odd" if it's odd.
def even_odd(number):
    if number%2==0:
        return "even"
    else:
        return "odd"
num=5
result=even_odd(num)
print("The number is:",result)