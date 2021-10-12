# # Python exercise
# # source - https://www.w3resource.com/python-exercises/python-basic-exercises.php
# # Python Basic (Part -I) - Exercises, Practice, Solution
# # Write a Python program to find whether a given number (accept from the user) is even or odd,
# # print out an appropriate message to the user.
# # Exercise 21

number = int(input("Input the number: "))


def even_or_odd(numb):
    modulo = numb % 2
    if modulo != 0:
        print("Number", numb, "is odd.")
    else:
        print("Number", numb, "is even.")


even_or_odd(number)
