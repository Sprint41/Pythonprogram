#: Create a variable inside a function and attempt to access it outside the function.
def myfunc():
    variable=54
    return variable
print(myfunc())
print(variable)