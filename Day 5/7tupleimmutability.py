# Attempt to change the name of a month in the tuple. Observe and explain the error that occurs.
mytuple=("January","February","March","April","May","June","July","August","September","October","November","December")
try:
    mytuple[2]="July"
except TypeError as e:
    print("Error:",e)