# Call a function with incorrect argument types and observe the error messages.
def sum(a,b,c):
    sum= a+b+c
    return sum
arguments= (7,8,"sum")
sum_result=sum(*arguments)
print("The sum is:",sum_result)
