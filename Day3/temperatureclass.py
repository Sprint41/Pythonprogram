# Request a temperature value from the user. Classify it as "hot" if it's above 30°C, "moderate" if between 20°C and 30°C, and "cold" if below
#20°C using if-else statements. Print the classification.
temperature= float(input("Enter temperature value:"))
if temperature>30:
    print("The weather is hot")
if temperature== 20<=temperature<=30:
    print("The weather is moderate")
if temperature<20:
    print("The weather is cold")
    