# Create multiple functions with the same name but different numbers of arguments.
def detail(name="Smith",age=18,standard=12):
    print("name:",name)
    print("age:",age)
    print("standard:",standard)
def detail(room_no=312,room_owner="Aditya",location="Pune"):
    print("room number:",room_no)
    print("room owner:",room_owner)
    print("location:",location)
detail()