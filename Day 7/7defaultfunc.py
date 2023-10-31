# Define a function with default parameters and call it with and without providing arguments.
def welcome(name="user",greeting="welcome to the programming world!!!"):
    return(greeting,name)
print(welcome("Aditya","Hi"))
print(welcome())