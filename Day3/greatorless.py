# Ask the user for their age and compare it to 18 using the greater than (>) and less than (<) operators. Print whether they are older or younger
# than 18.
input1= int(input("enter the age:"))
if input1>18:
    print("They are older than 18")
elif input1<18:
    print("They are smaller than 18")
else:
    print("They are same as 18")