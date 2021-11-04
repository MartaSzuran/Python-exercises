# # Python exercise
# # source - https://www.w3resource.com/python-exercises/python-basic-exercises.php
# # Python Basic (Part -I) - Exercises, Practice, Solution
# # Write a Python program to display your details like name, age, address in three different lines
# # Exercise 37

name = input("Give me your name: ")
address = input("Give me your address: ")
age = input("Give me your age: ")


def personal_data(user_name, user_address, user_age):
    print("Name: ", user_name, "\nAddress: ", user_address, "\nAge: ", user_age)
    # using .format
    print("Name: {}\nAge: {}\nAddress: {}".format(user_name, user_address, user_age))


personal_data(name, address, age)
