# Find and print the items that are in the fruits set but not in the vegetables set.
fruits={"apple","banana","mango","cherry","pineapple","strawberry"}
vegetable={"carrot","brocolli","cauliflower","ladyfinger","eggplant","cucumber","apple","corn"}
set_diff=fruits.difference(vegetable)
print("The items that are in fruits but not in vegetables set are",set_diff)