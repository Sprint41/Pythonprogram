# Call a function by unpacking a list or tuple as its arguments.
def sum(a,b,c):
    sum= a+b+c
    return sum
arguments= (7,8,9)
sum_result=sum(*arguments)
print("The sum is:",sum_result)