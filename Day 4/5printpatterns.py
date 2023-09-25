# Create a pattern using nested for loops, such as a triangle or a square, and print it.
sides= int(input("no of sides:"))
for p in range(1,sides+1):
    for q in range(p):
        print("*",end=" ")
    print("")
