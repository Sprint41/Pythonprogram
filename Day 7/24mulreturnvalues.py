# Define a function that returns multiple values (e.g., a tuple) and unpack them into variables.
def personal_info():
    name="smith"
    age=20
    place="pune"
    return name, age, place
person_name,person_age,person_location= personal_info()
print("name:",person_name)
print("age:",person_age)
print("place:",person_location)