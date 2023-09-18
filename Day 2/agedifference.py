#Take the ages of two people as input and calculate the age difference between them. Print a message stating who is older and by how many years.
age1= int(input("Enter first age:"))
age2= int(input("Enter second age:"))
if age1>age2:
    print("first user is older than second user")
    print("first user is older by:",age1-age2,"years")
else:
    print("second user is older than first user")
    print("second user is older by:",age2-age1,"years")