# Align text to the left, right, or center within a specified width.
greetings="Hello, World!"
width=40
left_align=greetings.ljust(width)
right_align=greetings.rjust(width)
center_align=greetings.center(width)
print("Left aligned word is: ",left_align)
print("Right aligned word is: ",right_align)
print("Centered aligned word is: ",center_align)