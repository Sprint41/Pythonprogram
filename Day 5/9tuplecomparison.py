# Compare two tuples containing the same months but in different orders. Determine if they are equal.
mytuple=("January","February","March","April","May","June","July","August","September","October","November","December")
mytuple1=("March","January","February","April","August","May","June","July","September","December","October","November")
equal= mytuple==mytuple1
print("Are the tuple equal?",equal)