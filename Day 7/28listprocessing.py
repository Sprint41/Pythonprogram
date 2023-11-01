# Write a function that processes a list and returns a modified version of the list.
def mod_list(input_list):
    modified_list=[element*2 for element in input_list]
    return modified_list
list=[1,2,3,4,5]
double_list=mod_list(list)
print("Original list:",list)
print("modified list:",double_list)