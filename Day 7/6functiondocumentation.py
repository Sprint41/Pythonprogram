#  Add a docstring to a custom function explaining what it does.
def calculate_average(numbers):
    if not numbers:
        raise   ValueError("The input list numbers is empty.")
    total=sum(numbers)
    average=total/len(numbers)
    return average
numbers=[1,2,3,4,5]
print(calculate_average(numbers))