def input_name():
    while True:
        name = input("Enter your name: ")
        if name.isalpha():
            return name
        else:
            print("Invalid input. Please enter letters only.")

user_name = input_name()

try: 
    user_age = int(input("Enter your age: "))
except ValueError:
    print("Error: please, write number")

def input_colour():
    while True:
        colour = input("Enter your favorite colour: ")
        if colour.isalpha():
            return colour
        else:
            print("Invalid input. Please enter letters only.")

user_fav_colour = input_colour()

with open("user_info.txt", "w") as file:
    file.write(f"Name - {user_name}, Age - {user_age}, Favourite Colour - {user_fav_colour}")
with open("user_info.txt", "r") as file:
    content = file.read()

answer = input("You want to read the written file?: ")
if answer == "yes":
    print(content)